"""Structural/PDF verification. This is deliberately NOT the UGREEN checker."""
from pathlib import Path, PurePosixPath
import hashlib
import json
import re
import stat
import sys
import zipfile
from official_authoring import VERSION

ROOT = Path(__file__).resolve().parents[1]
SLUGS = ("tacit","off-camera","contextcut","benchmatch")
ARCHIVED = ("lottrace","date-detective","continuity-desk","sharescope")
MAX_FILE, MAX_PACKAGE = 1_000_000, 10_000_000


def count_words(value):
    return max(len(value.split()),len(re.findall(r"[A-Za-z0-9]+(?:['-][A-Za-z0-9]+)*",value)))


def digest(value):
    return hashlib.sha256(value).hexdigest()


def normal(value):
    return re.sub(r"\s+"," ",value).strip()


def validate_skill(slug):
    folder=ROOT/"products"/slug/"skill"/slug
    entry=(folder/"SKILL.md").read_text()
    front=re.match(r"\A---\nname: ([a-z0-9]+(?:-[a-z0-9]+)*)\ndescription: (.+)\n---\n",entry)
    assert front, f"{slug}: expected exact two-field frontmatter"
    assert front[1]==slug and 2<=len(front[1])<=64
    description=json.loads(front[2])
    assert isinstance(description,str) and 0<len(description)<=1024
    for heading in ("# Goal","# Required input","# Generation-time capability evidence",
                    "# Orchestration","# Completion and failure"):
        assert heading in entry, (slug,heading)
    for state in ("completed","failed","cancelled","waiting_user","waiting_approval"):
        assert state in entry, (slug,state)
    assert not re.search(r"\b(?:TODO|TBD)\b",entry)
    actual={p.relative_to(folder).as_posix():p.read_bytes()
            for p in folder.rglob("*") if p.is_file()}
    assert len(actual)==7 and len(actual)<=100
    refs={name for name in actual if name.startswith("references/")}
    linked=set(re.findall(r"\]\((references/[^)]+)\)",entry))
    assert refs==linked, f"{slug}: each reference must be directly linked"
    for name,data in actual.items():
        assert len(data)<=MAX_FILE
        assert name=="SKILL.md" or (name.startswith("references/") and name.endswith(".md"))
        assert b"\0" not in data
    archive=ROOT/"deliverables"/slug/("v"+VERSION)/f"{slug}-initial-skill.zip"
    assert archive.stat().st_size<=MAX_PACKAGE
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        infos=z.infolist()
        assert len(infos)<=100 and sum(i.file_size for i in infos)<=MAX_PACKAGE
        assert len({i.filename.casefold() for i in infos})==len(infos)
        reconstructed={}
        for i in infos:
            path=PurePosixPath(i.filename)
            assert not path.is_absolute() and ".." not in path.parts and "\\" not in i.filename
            assert path.parts[0]==slug and not (i.flag_bits & 1)
            assert not stat.S_ISLNK(i.external_attr>>16)
            assert i.file_size<=MAX_FILE
            reconstructed[PurePosixPath(*path.parts[1:]).as_posix()]=z.read(i)
        assert reconstructed==actual, f"{slug}: ZIP must match current source exactly"
    for origin in ("source","extracted-zip"):
        check=json.loads((ROOT/"validation"/"official"/("v"+VERSION)/origin/(slug+".json")).read_text())
        assert check["status"]=="static-pass"
        assert check["summary"]=={"errors":0,"warnings":0,"info":0}
        assert check["catalog"]["checkedVersion"]=="2.0.0"
        recorded={item["path"]:item["sha256"] for item in check["files"]}
        assert recorded=={name:digest(data) for name,data in actual.items()}, (slug,"official evidence is stale")
    return {"files":len(actual),"source_bytes":sum(map(len,actual.values())),
            "zip_bytes":archive.stat().st_size,"zip_sha256":digest(archive.read_bytes()),
            "entry_sha256":digest((folder/"SKILL.md").read_bytes())}


def validate_proposal(slug):
    from pypdf import PdfReader
    data=json.loads((ROOT/"products"/slug/"proposal-answers.json").read_text())
    assert len(data["questions"])==len(data["answers"])==10
    word_count=sum(count_words(a) for a in data["answers"])
    assert word_count==data["word_count"] and word_count<=500
    pdf=ROOT/"deliverables"/slug/("v"+VERSION)/f"{slug}-proposal.pdf"
    assert pdf.stat().st_size<=MAX_FILE
    reader=PdfReader(pdf,strict=True)
    assert not reader.is_encrypted and len(reader.pages)==2
    extracted=normal(" ".join(page.extract_text() or "" for page in reader.pages))
    for question,answer in zip(data["questions"],data["answers"]):
        assert normal(question) in extracted, (slug,"missing PDF question",question)
        assert normal(answer) in extracted, (slug,"missing/mismatched PDF answer")
    assert "Third-party information" in extracted
    return {"substantive_words":word_count,"pdf_pages":len(reader.pages),
            "pdf_bytes":pdf.stat().st_size,"pdf_sha256":digest(pdf.read_bytes())}


def validate_links():
    checked=0
    for file in ROOT.rglob("*.md"):
        if ".git" in file.parts: continue
        for link in re.findall(r"(?<!!)\[[^\]]+\]\(([^)]+)\)",file.read_text()):
            if re.match(r"^[a-z]+:",link) or link.startswith("#"): continue
            target=link.split("#")[0]
            assert (file.parent/target).resolve().exists(), (str(file.relative_to(ROOT)),target)
            checked+=1
    return checked


def main():
    path=ROOT/"validation"/"local-checks.json"
    path.parent.mkdir(exist_ok=True)
    path.write_text(json.dumps({"result":"running","scope":"Local structural/PDF checks"})+"\n")
    try:
        results={slug:{"package":validate_skill(slug),"proposal":validate_proposal(slug)}
                 for slug in SLUGS}
        for slug in ARCHIVED:
            names={f.name for f in (ROOT/"concepts"/slug).iterdir()}
            assert names=={"README.md","demo.html"},(slug,names)
        assert len(list((ROOT/"demos").glob("*.html")))==9
        links=validate_links()
        report={
            "scope":"Local structural/PDF checks only; not the official UGREEN checker or NAS execution",
            "result":"passed","products":results,"local_markdown_links_checked":links,
            "archived_concepts":"exactly README.md and demo.html",
            "release":VERSION,
            "official_creation_tool":"supplied toolkit 0.7.3 used for authoring",
            "official_catalog_bindings":"checked against catalog 2.0.0",
            "official_checker":"static-pass, zero diagnostics; source and extracted ZIP hashes verified",
            "nas_runtime":"not run",
            "remote_publication":"not verified",
        }
        path.write_text(json.dumps(report,indent=2)+"\n")
        print(json.dumps({"result":"passed","products":len(results),
                          "links_checked":links,"report":str(path)},indent=2))
    except (AssertionError,ValueError,ImportError) as error:
        path.write_text(json.dumps({"result":"failed","error":repr(error),
                                   "scope":"Local structural/PDF checks only"},indent=2)+"\n")
        print("Local validation failed:",repr(error),file=sys.stderr)
        return 1
    return 0


if __name__=="__main__":
    raise SystemExit(main())
