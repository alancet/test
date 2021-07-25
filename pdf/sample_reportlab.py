from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4, portrait
from reportlab.lib.units import inch, mm, cm


cv = canvas.Canvas('test.pdf', pagesize=portrait(A4))

cv.rect(10*mm, 250*mm, 30*mm, 30*mm)
cv.line(10*mm, 220*mm, 200*mm, 220*mm)

xlist = (10*mm, 80*mm, 200*mm)
ylist = (200*mm, 170*mm, 140*mm)
cv.grid(xlist, ylist)

cv.showPage()
cv.save()
