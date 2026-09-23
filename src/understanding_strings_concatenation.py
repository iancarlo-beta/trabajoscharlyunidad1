# combinacion o concatenacion de STRING
first_name = 'ian'
last_name = "beta"
full_name = first_name + " " +  last_name
print(full_name)

print("hola", "ian" + " " + "beta", first_name.title() + " " + last_name.title())

message = "!hola, "  + full_name.title() + "!"
print(message)

# WhiteSpace
"""
whitespace se refiere a cualquier string 
(caracter) que no se imprime es decir un
espacio (" "), tabuladores 


"""





print("python")
print("\tpython")
print("\t\tpython")
print("lenguajes \n\tpython\n\tC\njavaScript")


# f-strings
famous_person = "iancarlobeta"
message = f"{famous_person} una vez dijo: python es amor"
print(message)