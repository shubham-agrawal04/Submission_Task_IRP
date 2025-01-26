from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_resume(output_file, font_size, font_color, bg_color):
    doc = SimpleDocTemplate(output_file, pagesize=letter)


    def draw_background(canvas_obj, doc):
        canvas_obj.setFillColor(bg_color)
        canvas_obj.rect(0, 0, letter[0], letter[1], fill=1)

    doc.build([Spacer(1, 1)], onFirstPage=draw_background, onLaterPages=draw_background)

    styles = getSampleStyleSheet()


    title_style = ParagraphStyle(
        "Title",
        fontName="Helvetica-Bold",
        fontSize=font_size + 2,
        textColor=font_color,
        spaceAfter=6,
    )
    subtitle_style = ParagraphStyle(
        "Subtitle",
        fontName="Helvetica",
        fontSize=font_size,
        textColor=font_color,
        spaceAfter=6,
    )
    section_title_style = ParagraphStyle(
        "SectionTitle",
        fontName="Helvetica-Bold",
        fontSize=font_size,
        textColor=font_color,
        spaceAfter=4,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        fontName="Helvetica",
        fontSize=font_size-2,
        textColor=font_color,
        leftIndent=15,
        spaceAfter=3,
    )
    sub_bullet_style = ParagraphStyle(
        "SubBullet",
        fontName="Helvetica",
        fontSize=font_size-4,
        textColor=font_color,
        leftIndent=30,
        spaceAfter=2,
    )

    elements = []

    name = Paragraph("<b>XXXXXXXXX</b>", title_style)
    role = Paragraph("XXXXXXXX Year Undergraduate", subtitle_style)
    dept = Paragraph("Department of Computer Science and Engineering", subtitle_style)
    contact_info = Paragraph("abc.xyz@iitgn.ac.in     +91 9000000000", subtitle_style)
    elements.extend([name, role, dept, contact_info, Spacer(1, 10)])


    elements.append(Paragraph("EDUCATION", section_title_style))
    education_data = [
        ["Degree", "Institution", "CPI/%", "Year"],
        ["B.Tech", "XXXXXXXXX", "9.95", "2016 - Present"],
        ["Class XII", "XXXXXXXXX, Ahmedabad", "99.5", "2015 - 2016"],
        ["Class X", "XXXXXXXXXXX, Ahmedabad", "100", "2013 - 2014"],
    ]
    education_table = Table(education_data, colWidths=[100, 200, 80, 80])
    education_table.setStyle(
        TableStyle([
            ("BACKGROUND", (0, 0), (-1, 0), bg_color),
            ("TEXTCOLOR", (0, 0), (-1, 0), font_color),
            ("ALIGN", (0, 0), (-1, -1), "CENTER"),
            ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
            ("GRID", (0, 0), (-1, -1), 0.5, bg_color),
            ("TEXTCOLOR", (0, 1), (-1, -1), font_color),
            ("FONTNAME", (0, 1), (-1, -1), "Helvetica"),
        ])
    )
    elements.extend([education_table, Spacer(1, 10)])


    elements.append(Paragraph("INTERNSHIPS", section_title_style))
    internships = [
        Paragraph("• Internship 1: Software Developer Intern, ABC Corp (May - July 2024)", bullet_style),
        Paragraph("  ◦ Developed a machine learning model to predict user churn.", sub_bullet_style),
        Paragraph("  ◦ Achieved a 95% accuracy rate and reduced churn by 20%.", sub_bullet_style),
        Paragraph("• Internship 2: Research Intern, XYZ University (Dec 2023 - Jan 2024)", bullet_style),
        Paragraph("  ◦ Conducted research on optimizing algorithms for big data processing.", sub_bullet_style),
        Paragraph("  ◦ Published results in a peer-reviewed journal.", sub_bullet_style),
    ]
    elements.extend(internships + [Spacer(1, 10)])


    elements.append(Paragraph("PROJECTS", section_title_style))
    projects = [
        Paragraph("• Project 1: E-commerce Recommendation System", bullet_style),
        Paragraph("  ◦ Built a recommendation engine using collaborative filtering.", sub_bullet_style),
        Paragraph("  ◦ Improved recommendation accuracy by 15%.", sub_bullet_style),
        Paragraph("• Project 2: Real-Time Chat Application", bullet_style),
        Paragraph("  ◦ Developed a web-based chat app using Flask and WebSocket.", sub_bullet_style),
        Paragraph("  ◦ Scaled the system to handle 1,000 concurrent users.", sub_bullet_style),
    ]
    elements.extend(projects + [Spacer(1, 10)])


    elements.append(Paragraph("POSITIONS OF RESPONSIBILITY", section_title_style))
    positions = [
        Paragraph("• Secretary, Student Council, XXXXXXXXXXXX (2024)", bullet_style),
        Paragraph("  ◦ Organized technical and cultural fests with 5,000+ attendees.", sub_bullet_style),
        Paragraph("  ◦ Managed a budget of Rs 10,00,000 and secured sponsorships.", sub_bullet_style),
        Paragraph("• Team Lead, Robotics Club (2023 - 2024)", bullet_style),
        Paragraph("  ◦ Led a team of 10 students to design an autonomous drone.", sub_bullet_style),
        Paragraph("  ◦ Secured 1st place in the national robotics competition.", sub_bullet_style),
    ]
    elements.extend(positions + [Spacer(1, 10)])



    elements.append(Paragraph("ACHIEVEMENTS", section_title_style))
    achievements = [
        Paragraph(
            "• Secured All India Rank X in XYZ.", bullet_style
        ),
        Paragraph(
            "• Received ABC Award for outstanding performance.", bullet_style
        ),
    ]
    elements.extend(achievements + [Spacer(1, 10)])


    elements.append(Paragraph("SKILL SUMMARY", section_title_style))
    skills = [
        Paragraph("• Languages: Python, C, C++, Verilog.", bullet_style),
        Paragraph(
            "• Tools: Autodesk Inventor Professional, ISE Design Suite.",
            bullet_style,
        ),
    ]
    elements.extend(skills + [Spacer(1, 10)])


    elements.append(Paragraph("EXTRA-CURRICULAR ACTIVITIES", section_title_style))
    activities = [
        Paragraph(
            "• Participated in XYZ hackathon, securing second place.", bullet_style
        ),
        Paragraph(
            "• Member of the cultural club organizing XYZ events.", bullet_style
        ),
    ]
    elements.extend(activities + [Spacer(1, 10)])


    doc.build(elements)
    print(f"Resume generated successfully: {output_file}")


import argparse


parser = argparse.ArgumentParser(description="Generate a customizable resume")
parser.add_argument("--font-size", type=int, default=12, help="Font size for the text")
parser.add_argument("--font-color", type=str, default="#000000", help="Font color (e.g., hex code or color name)")
parser.add_argument("--background-color", type=str, default="#FFFFFF", help="Background color (e.g., hex code or color name)")

args = parser.parse_args()


font_color = colors.HexColor(args.font_color)
background_color = colors.HexColor(args.background_color)
font_size = args.font_size


create_resume("customized_resume.pdf", font_size, font_color, background_color)