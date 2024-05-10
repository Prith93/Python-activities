from reportlab.platypus import SimpleDocTemplate, Table, Paragraph, TableStyle
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
  
data = [
    [ "  Fruit name  ", "  Date  " , "  Quantity  " ,"  Price (Rs.)  " ],
    [ "  Apple  ","  10/3/24  ","  4 kg  ", "  550.00/-  "],
    [ "  Mango  ", "  10/3/24  ", "  6 kg  ", "  700.00/-  "],
    [ "  Banana  ", "  10/3/24  ", "  3 kg  ", "  200.00/-  "],
    [ "  Lichi  ", "  10/3/24  ", "  6 kg  ", "  300.00/-  "],
    [ "  Guava  ", "  10/3/24  ", "  2 kg  ", "  300.00/-  "],
    [ "  Peach  ", "  10/3/24  ", "  1 kg  ", "  200.00/-  "],
    [ "  Pomegranate  ", "  10/3/24  ", "  4 kg  ", "  250.00/-  "],
    [ "  Pears  ", "  10/3/24  ", "  2 kg  ", "  150.00/-  "],
    [ "  Watermelon  ", "  10/3/24  ", "  2 kg  ", "  300.00/-  "],
    [ "  Papaya  ", "  10/3/24  ", "  1 kg  ", "  250.00/-  "],
    [ "  Jackfruit  ", "  10/3/24  ", "  1 kg  ", "  100.00/-  "],
    [ "  Total  ", "", "", "  3,300.00/-  "], 
    [ "  Discount  ", "", "", "  -330.00/-  "],
    [ "  Total  ", "", "", "  2970.00/-  "],
]
  
pdf = SimpleDocTemplate( "ABC_fruitshop.pdf" , pagesize = A4 )
styles = getSampleStyleSheet()
  
# Top-level heading (Heading1)
head_style = styles[ "Heading1" ]


head_style.alignment = 1 # 0: left
  
head = Paragraph( "ABC FRUIT SHOP" , head_style )
  
# creates a Table Style object and in it
style = TableStyle(
    [
        ( "BOX" , ( 0, 0 ), ( -1, -1 ), 1 , colors.black ),
        ( "GRID" , ( 0, 0 ), ( 4 , 11 ), 1 , colors.black ),
        ( "BACKGROUND" , ( 0, 0 ), ( 3, 0 ), colors.cyan ),
        ( "TEXTCOLOR" , ( 0, 0 ), ( -1, 0 ), colors.black ),
        ( "ALIGN" , ( 0, 0 ), ( -1, -1 ), "CENTER" ),
        ( "BACKGROUND" , ( 0 , 1 ) , ( -1 , -1 ), colors.pink ),
    ]
)
  
# creates a table object and passes the style to it
table = Table( data , style = style )

pdf.build([ head , table ])
