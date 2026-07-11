#!/usr/bin/env python3
"""Build the fixed-layout TNOA PDF from its Markdown source.

The renderer intentionally uses standard PDF fonts, deterministic metadata,
ASCII-safe compressed streams, and no interactive annotations.
"""

from pathlib import Path
import argparse
import re


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("source", type=Path, help="Markdown source path")
    parser.add_argument("output", type=Path, help="PDF output path")
    return parser.parse_args()


args = parse_args()
source_path = args.source
output_path = args.output
output_path.parent.mkdir(parents=True, exist_ok=True)
md = source_path.read_text(encoding="utf-8")

# The repository specification is intentionally ASCII-safe so that the
# generated PDF remains portable through text-oriented connector tooling.
md.encode("ascii")

# PDF generation using ReportLab with standard fonts and ASCII-safe compressed streams.
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import (
    BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, PageBreak,
    Table, TableStyle, Preformatted, ListFlowable, ListItem
)


class SpecDocTemplate(BaseDocTemplate):
    def __init__(self, filename, **kw):
        super().__init__(filename, **kw)
        frame = Frame(self.leftMargin, self.bottomMargin, self.width, self.height, id="normal")
        self.addPageTemplates(PageTemplate(id="main", frames=frame, onPage=self._header_footer))

    def _header_footer(self, canvas, doc):
        canvas.saveState()
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(colors.HexColor("#5B6470"))
        if doc.page > 1:
            canvas.drawString(
                self.leftMargin,
                0.45 * inch,
                "Tessera Normative Orientation Architecture - Version 0.1 Provisional",
            )
            canvas.drawRightString(
                letter[0] - self.rightMargin,
                0.45 * inch,
                f"Page {doc.page}",
            )
        canvas.restoreState()

    def afterFlowable(self, flowable):
        return


styles = getSampleStyleSheet()
styles.add(
    ParagraphStyle(
        name="TitleSpec",
        parent=styles["Title"],
        fontName="Helvetica-Bold",
        fontSize=23,
        leading=28,
        textColor=colors.HexColor("#173A5E"),
        alignment=TA_CENTER,
        spaceAfter=18,
    )
)
styles.add(
    ParagraphStyle(
        name="SubtitleSpec",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=13,
        leading=18,
        textColor=colors.HexColor("#4C5967"),
        alignment=TA_CENTER,
        spaceAfter=12,
    )
)
styles.add(
    ParagraphStyle(
        name="Meta",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9.5,
        leading=14,
        alignment=TA_CENTER,
        textColor=colors.HexColor("#343B44"),
    )
)
styles.add(
    ParagraphStyle(
        name="H1",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        leading=20,
        textColor=colors.HexColor("#173A5E"),
        spaceBefore=14,
        spaceAfter=8,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="H2",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=12.5,
        leading=16,
        textColor=colors.HexColor("#24557E"),
        spaceBefore=11,
        spaceAfter=6,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="H3",
        parent=styles["Heading3"],
        fontName="Helvetica-Bold",
        fontSize=10.5,
        leading=14,
        textColor=colors.HexColor("#334E68"),
        spaceBefore=8,
        spaceAfter=4,
        keepWithNext=True,
    )
)
styles.add(
    ParagraphStyle(
        name="BodySpec",
        parent=styles["BodyText"],
        fontName="Helvetica",
        fontSize=9.2,
        leading=13.2,
        spaceAfter=5,
        textColor=colors.HexColor("#20262D"),
    )
)
styles.add(
    ParagraphStyle(
        name="QuoteSpec",
        parent=styles["BodyText"],
        fontName="Helvetica-Oblique",
        fontSize=10,
        leading=14,
        leftIndent=18,
        rightIndent=18,
        borderColor=colors.HexColor("#8CA6BF"),
        borderWidth=1,
        borderPadding=8,
        backgroundColor=colors.HexColor("#F4F7FA"),
        spaceBefore=6,
        spaceAfter=8,
    )
)
styles.add(
    ParagraphStyle(
        name="CodeSpec",
        parent=styles["Code"],
        fontName="Courier",
        fontSize=7.5,
        leading=10,
        leftIndent=8,
        rightIndent=8,
        borderColor=colors.HexColor("#D7DEE5"),
        borderWidth=0.5,
        borderPadding=6,
        backgroundColor=colors.HexColor("#F7F8FA"),
        spaceBefore=5,
        spaceAfter=7,
    )
)
styles.add(
    ParagraphStyle(
        name="TOCHeading",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=16,
        textColor=colors.HexColor("#173A5E"),
        spaceAfter=10,
    )
)


def esc(text):
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def inline(text):
    text = esc(text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", text)
    text = re.sub(r"`([^`]+)`", r'<font name="Courier">\1</font>', text)
    return text


lines = md.splitlines()
story = []
story.append(Spacer(1, 0.75 * inch))
story.append(Paragraph("Tessera Normative Orientation Architecture", styles["TitleSpec"]))
story.append(
    Paragraph("Development and Holistic Measurement Specification", styles["SubtitleSpec"])
)
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("Document ID: TNOA-DMS-0.1", styles["Meta"]))
story.append(Paragraph("Version: 0.1 Provisional", styles["Meta"]))
story.append(Paragraph("Date: 2026-07-11", styles["Meta"]))
story.append(Paragraph("Status: Active / Provisional / Expansion Scaffold", styles["Meta"]))
story.append(Spacer(1, 0.45 * inch))
callout = Table(
    [[Paragraph(
        "<b>Purpose</b><br/>Define the staged development, independent construct analysis, semantic representation, measurement strategy, and validation plan for the Tessera Normative Orientation Architecture.",
        styles["BodySpec"],
    )]],
    colWidths=[5.9 * inch],
)
callout.setStyle(
    TableStyle(
        [
            ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#EEF4F8")),
            ("BOX", (0, 0), (-1, -1), 1, colors.HexColor("#7C9BB8")),
            ("LEFTPADDING", (0, 0), (-1, -1), 12),
            ("RIGHTPADDING", (0, 0), (-1, -1), 12),
            ("TOPPADDING", (0, 0), (-1, -1), 10),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
        ]
    )
)
story.append(callout)
story.append(PageBreak())
story.append(Paragraph("Contents Overview", styles["TOCHeading"]))
for entry in [
    "1. Executive summary and scientific position",
    "2. Governing construct, scope, and layered architecture",
    "3. Bioecological organization",
    "4. Independent construct workstreams",
    "5. Cross-cutting axes and Construct Development Packet",
    "6. Normative Decision Episode and graph implementation",
    "7. Measurement battery and Tessera integration",
    "8. Scoring policy, validation roadmap, and profile output",
    "9. Repository implementation, risks, and appendices",
]:
    story.append(Paragraph(entry, styles["BodySpec"]))
story.append(PageBreak())

start = 0
for i, line in enumerate(lines):
    if line.strip() == "---":
        start = i + 1
        break
lines = lines[start:]

i = 0
while i < len(lines):
    line = lines[i]
    s = line.strip()
    if not s:
        i += 1
        continue
    if s == "---":
        story.append(Spacer(1, 6))
        i += 1
        continue
    if s.startswith("```"):
        buf = []
        i += 1
        while i < len(lines) and not lines[i].strip().startswith("```"):
            buf.append(lines[i])
            i += 1
        i += 1
        story.append(Preformatted("\n".join(buf), styles["CodeSpec"]))
        continue
    if s.startswith("> "):
        quote = []
        while i < len(lines) and lines[i].strip().startswith("> "):
            quote.append(lines[i].strip()[2:])
            i += 1
        story.append(Paragraph(inline(" ".join(quote)), styles["QuoteSpec"]))
        continue
    if s.startswith("# "):
        story.append(Paragraph(inline(s[2:]), styles["H1"]))
        i += 1
        continue
    if s.startswith("## "):
        story.append(Paragraph(inline(s[3:]), styles["H2"]))
        i += 1
        continue
    if s.startswith("### "):
        story.append(Paragraph(inline(s[4:]), styles["H3"]))
        i += 1
        continue
    if s.startswith("|") and i + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-+", lines[i + 1]):
        rows = []
        while i < len(lines) and lines[i].strip().startswith("|"):
            rows.append([c.strip() for c in lines[i].strip().strip("|").split("|")])
            i += 1
        if len(rows) >= 2:
            rows.pop(1)
        maxcols = max(len(row) for row in rows)
        data = []
        for row_number, row in enumerate(rows):
            row = row + [""] * (maxcols - len(row))
            cell_style = ParagraphStyle(
                name=f"TCell{row_number}",
                parent=styles["BodySpec"],
                fontSize=7.5,
                leading=9.5,
                textColor=colors.white if row_number == 0 else colors.HexColor("#20262D"),
            )
            data.append([Paragraph(inline(cell), cell_style) for cell in row])
        widths = [6.5 * inch / maxcols] * maxcols
        table = Table(data, colWidths=widths, repeatRows=1, hAlign="LEFT")
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#24557E")),
                    ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
                    ("GRID", (0, 0), (-1, -1), 0.35, colors.HexColor("#B8C4CE")),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 4),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                    ("TOPPADDING", (0, 0), (-1, -1), 4),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [colors.white, colors.HexColor("#F5F7F9")]),
                ]
            )
        )
        story.append(table)
        story.append(Spacer(1, 6))
        continue
    if re.match(r"^[-*] ", s):
        items = []
        while i < len(lines) and re.match(r"^\s*[-*] ", lines[i].strip()):
            items.append(
                ListItem(
                    Paragraph(inline(lines[i].strip()[2:]), styles["BodySpec"]),
                    leftIndent=10,
                )
            )
            i += 1
        story.append(
            ListFlowable(
                items,
                bulletType="bullet",
                leftIndent=18,
                bulletFontName="Helvetica",
                bulletFontSize=7,
                spaceAfter=5,
            )
        )
        continue
    if re.match(r"^\d+\. ", s):
        items = []
        while i < len(lines) and re.match(r"^\d+\. ", lines[i].strip()):
            text = re.sub(r"^\d+\.\s*", "", lines[i].strip())
            items.append(ListItem(Paragraph(inline(text), styles["BodySpec"]), leftIndent=12))
            i += 1
        story.append(
            ListFlowable(
                items,
                bulletType="1",
                leftIndent=20,
                bulletFontName="Helvetica",
                bulletFontSize=8,
                spaceAfter=5,
            )
        )
        continue

    buf = [s]
    i += 1
    while i < len(lines):
        next_line = lines[i].strip()
        if not next_line:
            break
        if (
            next_line == "---"
            or next_line.startswith("#")
            or next_line.startswith("```")
            or next_line.startswith("> ")
            or next_line.startswith("|")
            or re.match(r"^[-*] ", next_line)
            or re.match(r"^\d+\. ", next_line)
        ):
            break
        buf.append(next_line)
        i += 1
    story.append(Paragraph(inline(" ".join(buf)), styles["BodySpec"]))


doc = SpecDocTemplate(
    str(output_path),
    pagesize=letter,
    rightMargin=0.62 * inch,
    leftMargin=0.62 * inch,
    topMargin=0.68 * inch,
    bottomMargin=0.68 * inch,
    title="Tessera Normative Orientation Architecture Development Specification v0.1",
    author="Tessera Identity System",
    pageCompression=1,
    invariant=1,
)
doc.build(story)

# Replace ReportLab's binary marker with an equal-length ASCII marker so xref
# offsets remain valid while the complete PDF stays ASCII-safe.
pdf_bytes = output_path.read_bytes()
pdf_bytes = pdf_bytes.replace(
    b"%\x93\x8c\x8b\x9e ReportLab Generated PDF document",
    b"% ReportLab Generated PDF document    ",
)
try:
    pdf_bytes.decode("ascii")
except UnicodeDecodeError as exc:
    bad = sorted({byte for byte in pdf_bytes if byte > 127})
    raise RuntimeError(f"PDF contains non-ASCII bytes: {bad[:20]} at {exc.start}") from exc

output_path.write_bytes(pdf_bytes)
print(f"Wrote {output_path} ({output_path.stat().st_size} bytes, ASCII-only)")
