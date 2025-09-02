from reportlab.pdfgen import canvas

def generate_portfolio(student, achievements):
    filename = f"{student.name}_portfolio.pdf"
    c = canvas.Canvas(filename)
    c.drawString(100, 800, f"Portfolio: {student.name}")
    y = 760
    for a in achievements:
        c.drawString(100, y, f"{a.title} ({a.category}) - {a.status}")
        y -= 20
    c.save()
    return filename
