from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, ListFlowable, ListItem
from reportlab.lib import colors

out = "output/pdf/maya-schneider-cv.pdf"
doc = SimpleDocTemplate(out, pagesize=letter, rightMargin=.72*inch, leftMargin=.72*inch,
                        topMargin=.62*inch, bottomMargin=.58*inch)
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Name", parent=styles["Title"], fontName="Helvetica-Bold", fontSize=21, leading=25, textColor=colors.HexColor("#243447"), alignment=TA_LEFT, spaceAfter=3))
styles.add(ParagraphStyle(name="Contact", parent=styles["Normal"], fontSize=9.5, leading=12, textColor=colors.HexColor("#4d5b66"), spaceAfter=13))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading2"], fontName="Helvetica-Bold", fontSize=11.5, leading=14, textColor=colors.HexColor("#2f6175"), spaceBefore=9, spaceAfter=5))
styles.add(ParagraphStyle(name="Role", parent=styles["Heading3"], fontName="Helvetica-Bold", fontSize=10.4, leading=13, textColor=colors.HexColor("#243447"), spaceBefore=6, spaceAfter=1))
styles.add(ParagraphStyle(name="BodySmall", parent=styles["BodyText"], fontName="Helvetica", fontSize=9.25, leading=12.2, textColor=colors.HexColor("#333b40"), spaceAfter=3))
styles.add(ParagraphStyle(name="Meta", parent=styles["BodyText"], fontSize=8.9, leading=11, textColor=colors.HexColor("#68737a"), spaceAfter=4))

def bullets(items):
    return ListFlowable([ListItem(Paragraph(x, styles["BodySmall"]), leftIndent=9) for x in items], bulletType="bullet", start="circle", leftIndent=14, bulletFontName="Helvetica", bulletFontSize=6, bulletOffsetY=2, spaceAfter=2)

story = [Paragraph("Maya Schneider", styles["Name"]), Paragraph("Austin, TX · maya.schneider@example.com · (512) 555-0147", styles["Contact"])]
story += [Paragraph("ABOUT ME", styles["Section"]), Paragraph("I have worked in customer support for 10 years. I started in technical support and then worked in implementation and customer care. In my last job I was responsible for a team of 10 people. I moved to the United States recently and am now looking for a new job.", styles["BodySmall"])]
story += [Paragraph("PROFESSIONAL EXPERIENCE", styles["Section"])]

jobs = [
    ("Customer Care Lead", "Northstar Connect GmbH — Germany | 2022–2026", "Hybrid", ["Managed a team of 10 customer care specialists.", "Organized the daily work and helped with difficult customer cases.", "Spoke with team members about their work and helped them improve.", "Checked customer conversations and gave feedback.", "Worked with Product and Technical teams when customers reported recurring problems.", "Helped train new people joining the team."]),
    ("Customer Care Specialist", "Northstar Connect GmbH — Germany | 2020–2022", "Office-based", ["Answered customer questions by phone, chat, and email.", "Helped with account and product questions.", "Passed more complicated cases to the right person.", "Wrote notes about customer issues and common questions.", "Worked with other teams to solve customer problems."]),
    ("Implementation Manager", "CloudHarbor Software GmbH — Germany | 2017–2020", "Office-based", ["Worked with customers who were moving to the company’s software.", "Planned the migration steps and kept customers informed about the timing.", "Collected information needed for the migration.", "Explained the new system and helped customers learn how to use it.", "Worked with support and technical colleagues when there were problems."]),
    ("Technical Support Engineer", "CloudHarbor Software GmbH — Germany | 2014–2017", "Office-based", ["Answered technical support tickets by phone and chat.", "Looked into customer problems and tried to find a solution.", "Asked customers for more information when needed.", "Wrote notes about the issue and sent bugs to the technical team.", "Followed up with customers after the problem was fixed."]),
]
for role, company, mode, items in jobs:
    story += [Paragraph(role, styles["Role"]), Paragraph(company, styles["Meta"]), Paragraph(mode, styles["Meta"]), bullets(items)]

story += [Paragraph("SKILLS AND SOFTWARE", styles["Section"]), bullets(["Customer support by phone, chat, and email", "Working with ticket systems and customer records", "Troubleshooting and handling escalations", "Customer migrations", "Training new colleagues", "Salesforce", "Zendesk", "Jira", "Confluence", "Microsoft Office"])]
story += [Paragraph("EDUCATION", styles["Section"]), Paragraph("Bachelor of Business Administration", styles["Role"]), Paragraph("Fictional University of Applied Sciences — Germany", styles["Meta"])]
story += [Paragraph("LANGUAGES", styles["Section"]), Paragraph("German (native), English (good working knowledge)", styles["BodySmall"])]
doc.build(story)
