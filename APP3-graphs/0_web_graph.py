import justpy as jp         

#creating a quasar page(web page), justpy uses quaser script hence the name
def app():
    webp = jp.QuasarPage()                                                                       #creating object instance
    h1 = jp.QDiv(a=webp, text="Analysis", classes="text-h3 text-center q-pa-lg")                  #QDiv to add elements, 'a' parameter always used to connect element to web page
    p1 = jp.QDiv(a=webp, text="Course Reviews", classes="text-weight-bold text-left q-px-md")         #classes parameter to style the element(search quasar style on google to get text) 
    return webp

jp.justpy(app)                  #justpy method accepts func that returns quasar page