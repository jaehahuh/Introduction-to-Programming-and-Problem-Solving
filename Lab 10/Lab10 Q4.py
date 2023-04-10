def html_table_generator (lst, file_to_write_to):
    with open (file_to_write_to, "w") as f:
        print("<html>", file = f)
        print("\t <table>", file = f)
        print("\t\t <tr>", file = f)
        for i in (lst[0]):
            print ("\t\t\t", "<th>", i, "</th>", file = f)
        print("\t\t </tr>", file = f)
        print("\t\t <tr>", file = f)
        for i in (lst[1]):
            print ("\t\t\t", "<td>", i, "</td>", file = f)
        print("\t\t </tr>", file = f)        
        print("\t\t <tr>", file = f)
        for i in (lst[2]):
            print ("\t\t\t", "<td>", i, "</td>", file = f)
        print("\t\t </tr>", file = f)
        print("\t\t <tr>", file = f)
        for i in (lst[3]):
            print ("\t\t\t", "<td>", i, "</td>", file = f)
        print("\t\t </tr>", file = f)
        print("\t <table>", file = f)
        print("<html>", file = f)


def main():
    filename = "test.html"
    lst = [["Header 1", "Header 2", "Header 3", "Header 4"], ["R1C1", "R1C2", "R1C3", "R1C4"],
            ["R2C1", "R2C2", "R2C3", "R2C4"], ["R3C1", "R3C2", "R3C3", "R3C4"]]
    html_table_generator (lst, filename)

main()
