from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
from reportlab.lib.enums import TA_LEFT, TA_CENTER

doc = SimpleDocTemplate(
    "/home/user/coding/Muscle_Tissue_Practice_ANSWERS.pdf",
    pagesize=letter,
    rightMargin=0.75*inch,
    leftMargin=0.75*inch,
    topMargin=0.75*inch,
    bottomMargin=0.75*inch
)

styles = getSampleStyleSheet()

# Custom styles
title_style = ParagraphStyle('Title', parent=styles['Normal'],
    fontSize=12, fontName='Helvetica-Bold', spaceAfter=4)
topic_style = ParagraphStyle('Topic', parent=styles['Normal'],
    fontSize=11, fontName='Helvetica-Bold', spaceAfter=4, textColor=colors.HexColor('#1a1a8c'),
    underline=True)
heading_style = ParagraphStyle('Heading', parent=styles['Normal'],
    fontSize=10, fontName='Helvetica-Bold', spaceAfter=3, underline=True)
body_style = ParagraphStyle('Body', parent=styles['Normal'],
    fontSize=10, fontName='Helvetica', spaceAfter=2, leftIndent=10)
bullet_style = ParagraphStyle('Bullet', parent=styles['Normal'],
    fontSize=10, fontName='Helvetica', spaceAfter=2, leftIndent=20)
sub_bullet_style = ParagraphStyle('SubBullet', parent=styles['Normal'],
    fontSize=10, fontName='Helvetica', spaceAfter=2, leftIndent=40)
answer_style = ParagraphStyle('Answer', parent=styles['Normal'],
    fontSize=10, fontName='Helvetica-Bold', textColor=colors.HexColor('#c00000'), spaceAfter=2)
note_style = ParagraphStyle('Note', parent=styles['Normal'],
    fontSize=9, fontName='Helvetica-Oblique', textColor=colors.gray, leftIndent=40, spaceAfter=2)

def ans(text):
    return f'<font color="#c00000"><b>[{text}]</b></font>'

story = []

# ─────────────────────────────────────────────
# HEADER
# ─────────────────────────────────────────────
story.append(Paragraph("<b>Muscle Tissue Practice Supplement — ANSWER KEY</b>", title_style))
story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
story.append(Spacer(1, 6))

# ─────────────────────────────────────────────
# PAGE 1: STRUCTURE OF A SKELETAL MUSCLE
# ─────────────────────────────────────────────
story.append(Paragraph("TOPIC: STRUCTURE OF A SKELETAL MUSCLE", topic_style))
story.append(Paragraph("<b>The Muscle Fiber</b>", heading_style))

story.append(Paragraph(
    f"• For a muscle fiber to contract, the tissue must {ans('be stimulated / receive a signal')}.",
    bullet_style))

story.append(Paragraph(
    f"Sarco{ans('lemma')}: plasma membrane wrapping myo{ans('fibrils')}",
    bullet_style))
story.append(Paragraph(
    f"  ▪ <b>T-Tubules:</b> membrane {ans('invaginations / extensions')} that reach deep myofibrils.",
    sub_bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph(
    f"Myo{ans('fibrils')}: long, rod-shaped organelles.",
    bullet_style))
story.append(Paragraph(
    f"  ▪ Contain myo{ans('filaments')}.",
    sub_bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph(
    f"Myo{ans('filaments')}: Proteins: actin &amp; myosin.",
    bullet_style))
story.append(Paragraph(
    f"Sarco{ans('mere')}: Contractile {ans('unit')}.",
    bullet_style))
story.append(Paragraph(
    f"  ▪ Creates {ans('striated')} appearance.",
    sub_bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph(
    f"<b>Sarco{ans('plasmic')} Reticulum:</b> Endoplasmic reticulum of muscle cells.",
    bullet_style))
story.append(Paragraph("  ▪ Surrounds myofibrils.", sub_bullet_style))
story.append(Paragraph("  ▪ Store/release Ca²⁺ ions.", sub_bullet_style))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
story.append(Spacer(1, 6))

# ─────────────────────────────────────────────
# PAGE 2: SLIDING FILAMENT THEORY — BASICS
# ─────────────────────────────────────────────
story.append(Paragraph("TOPIC: SLIDING FILAMENT THEORY AND THE SARCOMERE", topic_style))
story.append(Paragraph("<b>Sliding Filament Theory</b>", heading_style))

story.append(Paragraph("• How do muscles get shorter?", bullet_style))
story.append(Paragraph(
    f"  ▪ <b>Myosin</b> ({ans('thick')} filament): anchored to the <i>center</i> of the sarcomere.",
    sub_bullet_style))
story.append(Paragraph(
    "    – Protein that wants to <i>pull on a rope</i>.",
    note_style))
story.append(Paragraph(
    f"  ▪ <b>Actin</b> ({ans('thin')} filament): anchored to the <i>ends</i> of the sarcomere.",
    sub_bullet_style))
story.append(Paragraph(
    f"    – Protein that is the {ans('rope')}.",
    note_style))

story.append(Spacer(1, 4))
story.append(Paragraph("• During contraction:", bullet_style))
story.append(Paragraph(
    f"  ▪ Filaments (actin &amp; myosin) stay the {ans('same')} length; "
    f"overlap of actin &amp; myosin {ans('increases')}.",
    sub_bullet_style))

story.append(Spacer(1, 6))
# Example box
example_data = [
    [Paragraph("<b>EXAMPLE — Sarcomere Labeling</b>", ParagraphStyle('ex', fontSize=10, fontName='Helvetica-Bold'))],
    [Paragraph(
        "1. Myosin filaments: the <b>thick</b> filaments in the center of each sarcomere (between Z-discs).",
        ParagraphStyle('exb', fontSize=10, fontName='Helvetica', leftIndent=10))],
    [Paragraph(
        "2. Actin filaments: the <b>thin</b> filaments extending from the Z-discs toward the center.",
        ParagraphStyle('exb', fontSize=10, fontName='Helvetica', leftIndent=10))],
    [Paragraph(
        f"3. When the muscle contracts, the {ans('actin')} filament gets closer to the center of the sarcomere.",
        ParagraphStyle('exb', fontSize=10, fontName='Helvetica', leftIndent=10))],
]
ex_table = Table(example_data, colWidths=[6.5*inch])
ex_table.setStyle(TableStyle([
    ('BOX', (0,0), (-1,-1), 1, colors.HexColor('#1a1a8c')),
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dce6f1')),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 8),
]))
story.append(ex_table)
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
story.append(Spacer(1, 6))

# ─────────────────────────────────────────────
# PAGE 3: PROTEINS OF THE SARCOMERE
# ─────────────────────────────────────────────
story.append(Paragraph("TOPIC: SLIDING FILAMENT THEORY AND THE SARCOMERE", topic_style))
story.append(Paragraph("<b>Proteins of the Sarcomere</b>", heading_style))

story.append(Paragraph(
    f"• <i>Recall:</i> Sarcomere is the contractile unit: {ans('myosin')} pulls on {ans('actin')}.",
    bullet_style))

story.append(Paragraph("• <b>Contractile Proteins:</b>", bullet_style))
story.append(Paragraph(
    f"  ▪ <b>Myosin:</b> {ans('thick')} filament: <i>many headed Medusa.</i>",
    sub_bullet_style))
story.append(Paragraph(
    f"  ▪ <b>Actin:</b> {ans('thin')} filament: <i>acTIN is THIN.</i>",
    sub_bullet_style))

story.append(Paragraph("• <b>Regulatory Proteins:</b>", bullet_style))
story.append(Paragraph(
    f"  ▪ <b>Tropomyosin:</b> {ans('rod')}-like protein, wraps actin.",
    sub_bullet_style))
story.append(Paragraph(
    f"    – {ans('Blocks / Covers')} the myosin binding sites on actin.",
    note_style))
story.append(Paragraph(
    f"  ▪ <b>Troponin:</b> {ans('regulatory')} protein.",
    sub_bullet_style))
story.append(Paragraph(
    f"    – Binds to Ca²⁺: {ans('exposes / uncovers')} the binding sites on actin by moving tropomyosin.",
    note_style))
story.append(Paragraph(
    '    \u2013 <i>Tropomyosin says "No" to the myosin.   TrOPONin OPENs the binding site.</i>',
    note_style))

story.append(Paragraph("• <b>Structural Proteins:</b>", bullet_style))
story.append(Paragraph(
    f"  ▪ <b>Elastic Filament</b> (Titin): helps sarcomere retain {ans('shape / elasticity')}.",
    sub_bullet_style))

story.append(Spacer(1, 10))
story.append(Paragraph("<b>Structure of the Sarcomere: Bands, Zones, Discs &amp; Lines</b>", heading_style))

story.append(Paragraph(
    f"• The regions of the sarcomere were named for how they {ans('appeared / looked')} on a TEM microscope.",
    bullet_style))

story.append(Paragraph("<b>1. Discs and Lines:</b>", bullet_style))
story.append(Paragraph(
    f"  ▪ {ans('Z')} Disc: end of sarcomere. <i>(Z is at the end of the alphabet.)</i>",
    sub_bullet_style))
story.append(Paragraph(
    f"  ▪ {ans('M')} Line: Myomesin protein that {ans('anchors')} myosin. <i>(M = Middle.)</i>",
    sub_bullet_style))

story.append(Paragraph("<b>2. Bands and Zones:</b>", bullet_style))
story.append(Paragraph(
    f"  ▪ <b>I band</b> ({ans('light')} Band): area with just {ans('actin')}.",
    sub_bullet_style))
story.append(Paragraph(
    f"  ▪ <b>A band</b> ({ans('dark')} Band): area with {ans('both')} actin &amp; myosin.",
    sub_bullet_style))
story.append(Paragraph(
    f"    – {ans('H')} Zone: center region with just {ans('myosin')}. <i>(Helle = bright.)</i>",
    note_style))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
story.append(Spacer(1, 6))

# ─────────────────────────────────────────────
# PAGE 4: STEPS OF MUSCLE CONTRACTION
# ─────────────────────────────────────────────
story.append(Paragraph("TOPIC: STEPS OF MUSCLE CONTRACTION", topic_style))

# Example table
story.append(Paragraph("<b>EXAMPLE — Sarcomere Regions During Contraction</b>", heading_style))
story.append(Paragraph(
    "a) Mark A Band, I Band, H Zone with brackets on the TEM image. "
    "b) Mark Z Disc and M Line with arrows. "
    "c) Draw a line = length of one Actin filament.",
    body_style))

table_data = [
    [Paragraph("<b>Structure</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold')),
     Paragraph("<b>Description</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold')),
     Paragraph("<b>Change in size during contraction</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold'))],
    ["A Band",
     "Region containing myosin (thick filaments); overlaps with actin at edges",
     Paragraph(f"{ans('No change — stays the same size')}", ParagraphStyle('td', fontSize=10, fontName='Helvetica'))],
    ["I Band",
     "Region with only actin (thin filaments), flanking the Z-disc",
     Paragraph(f"{ans('Decreases / gets smaller')}", ParagraphStyle('td', fontSize=10, fontName='Helvetica'))],
    ["H Zone",
     "Center of A band; only myosin, no actin overlap",
     Paragraph(f"{ans('Decreases / gets smaller')}", ParagraphStyle('td', fontSize=10, fontName='Helvetica'))],
    ["Z Disc",
     "Boundary/end of each sarcomere; actin anchored here",
     Paragraph(f"{ans('Move closer together')}", ParagraphStyle('td', fontSize=10, fontName='Helvetica'))],
    ["M Line",
     "Center of sarcomere; myosin anchored here",
     Paragraph(f"{ans('No change — stays the same')}", ParagraphStyle('td', fontSize=10, fontName='Helvetica'))],
]
t = Table(table_data, colWidths=[0.9*inch, 2.8*inch, 2.8*inch])
t.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dce6f1')),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
]))
story.append(t)
story.append(Spacer(1, 8))

story.append(Paragraph("<b>Overview of Muscle Contraction</b>", heading_style))
story.append(Paragraph(
    f"• Muscle contraction involves the {ans('transmission of a signal via the')} nervous "
    f"{ans('system')}, initiating an action potential.",
    bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph(
    f"<b>A.</b> At the neuro-muscular junction, muscle cell is stimulated "
    f"by the {ans('nervous')} system, initiating an action potential.",
    bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph("<b>B. Excitation-Contraction Coupling:</b>", bullet_style))
story.append(Paragraph(
    f"  ▪ Action potential {ans('propagates')} along the sarcolemma and enters the "
    f"{ans('T')}-tubules.",
    sub_bullet_style))
story.append(Paragraph(
    f"  ▪ Sarcoplasmic reticulum releases {ans('Ca²⁺')}; "
    f"{ans('myosin')} binding sites are exposed.",
    sub_bullet_style))

story.append(Spacer(1, 4))
story.append(Paragraph(
    f"<b>C.</b> Myosin binds to {ans('actin')}, forming a "
    f"{ans('cross')}bridge and performs the <b>power stroke</b>.",
    bullet_style))

story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=0.5, color=colors.lightgrey))
story.append(Spacer(1, 6))

# ─────────────────────────────────────────────
# PAGE 5: NEUROTRANSMITTERS & ACTION POTENTIALS
# ─────────────────────────────────────────────
story.append(Paragraph("TOPIC: STEPS OF MUSCLE CONTRACTION", topic_style))
story.append(Paragraph("<b>Neurotransmitters &amp; Action Potentials</b>", heading_style))

# Example classify table
story.append(Paragraph(
    "<b>EXAMPLE — Classify each structure (T = transfers signal, R = regulates contraction, C = directly active in mechanics):</b>",
    body_style))

classify_data = [
    [Paragraph("<b>Structure</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold')),
     Paragraph("<b>Answer</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold')),
     Paragraph("<b>Reason</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold'))],
    ["1. Actin",
     Paragraph(ans("C"), ParagraphStyle('td', fontSize=10)),
     "Directly performs contraction (thin filament pulled by myosin)"],
    ["2. Calcium ions",
     Paragraph(ans("R"), ParagraphStyle('td', fontSize=10)),
     "Binds troponin to regulate (expose) myosin binding sites"],
    ["3. Myosin",
     Paragraph(ans("C"), ParagraphStyle('td', fontSize=10)),
     "Directly performs contraction (power stroke)"],
    ["4. Sarcolemma",
     Paragraph(ans("T"), ParagraphStyle('td', fontSize=10)),
     "Transfers action potential along muscle cell surface"],
    ["5. Sarcoplasmic reticulum",
     Paragraph(ans("T"), ParagraphStyle('td', fontSize=10)),
     "Transfers/delivers Ca²⁺ signal into the cell interior"],
    ["6. Troponin",
     Paragraph(ans("R"), ParagraphStyle('td', fontSize=10)),
     "Regulatory protein — opens binding sites when Ca²⁺ binds"],
    ["7. Tropomyosin",
     Paragraph(ans("R"), ParagraphStyle('td', fontSize=10)),
     "Regulatory protein — blocks/unblocks actin binding sites"],
    ["8. T tubule",
     Paragraph(ans("T"), ParagraphStyle('td', fontSize=10)),
     "Transfers action potential deep into the muscle fiber"],
]
ct = Table(classify_data, colWidths=[1.5*inch, 0.8*inch, 4.2*inch])
ct.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dce6f1')),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
]))
story.append(ct)
story.append(Spacer(1, 8))

story.append(Paragraph("<b>Neurotransmitters &amp; Action Potentials — Filled Blanks</b>", heading_style))

story.append(Paragraph(
    f"• <b>Synapse:</b> {ans('gap / space')} between the axon and the muscle.",
    bullet_style))
story.append(Paragraph(
    f"• <b>Acetylcholine:</b> neurotransmitter of the neuromuscular junction.",
    bullet_style))
story.append(Paragraph(
    f"• <b>Neurotransmitters:</b> chemical messengers used at {ans('synapses / the NMJ')}.",
    bullet_style))

story.append(Spacer(1, 6))
story.append(Paragraph("<b>Action Potential — Depolarization &amp; Repolarization:</b>", bullet_style))
story.append(Paragraph(
    f"• Change of polarization caused by movement of Na⁺ and K⁺.",
    bullet_style))

ap_data = [
    [Paragraph("<b>State</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold')),
     Paragraph("<b>Ion movement</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold')),
     Paragraph("<b>Result</b>", ParagraphStyle('th', fontSize=10, fontName='Helvetica-Bold'))],
    ["Polarized (resting)",
     Paragraph(f"Na⁺ {ans('outside')} cell; K⁺ {ans('inside')} cell", ParagraphStyle('td', fontSize=10)),
     "Outside positive, inside negative"],
    ["Depolarization",
     Paragraph(f"Na⁺ {ans('moves inside')}", ParagraphStyle('td', fontSize=10)),
     "Inside cell becomes more positive"],
    ["Repolarization",
     Paragraph(f"K⁺ {ans('moves outside')}", ParagraphStyle('td', fontSize=10)),
     "Charge is restored (resting state returns)"],
]
apt = Table(ap_data, colWidths=[1.5*inch, 2.5*inch, 2.5*inch])
apt.setStyle(TableStyle([
    ('BACKGROUND', (0,0), (-1,0), colors.HexColor('#dce6f1')),
    ('FONTNAME', (0,0), (-1,0), 'Helvetica-Bold'),
    ('FONTSIZE', (0,0), (-1,-1), 10),
    ('BOX', (0,0), (-1,-1), 1, colors.black),
    ('INNERGRID', (0,0), (-1,-1), 0.5, colors.grey),
    ('VALIGN', (0,0), (-1,-1), 'MIDDLE'),
    ('TOPPADDING', (0,0), (-1,-1), 4),
    ('BOTTOMPADDING', (0,0), (-1,-1), 4),
    ('LEFTPADDING', (0,0), (-1,-1), 4),
]))
story.append(apt)
story.append(Spacer(1, 10))
story.append(HRFlowable(width="100%", thickness=1, color=colors.black))
story.append(Spacer(1, 4))
story.append(Paragraph(
    "<i>All answers shown in red. Original worksheet: Muscle Tissue Practice Supplement.</i>",
    ParagraphStyle('footer', fontSize=9, fontName='Helvetica-Oblique', textColor=colors.grey, alignment=TA_CENTER)
))

doc.build(story)
print("PDF created: Muscle_Tissue_Practice_ANSWERS.pdf")
