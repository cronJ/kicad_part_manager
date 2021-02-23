import os

import pyparsing as pp

PROJECT_FOLDER = "C:\\Users\\priva\\OneDrive\\Dokumente\\kicad\projects\\test_5_99\\test"


def update_schematic(part, sch_file):
    with open(sch_file, 'r') as stream:
        try:
            schematic = stream.read()

            # S-expression grammar
            w = pp.Word(pp.alphanums)
            lp = pp.Suppress("(")
            rp = pp.Suppress(")")
            sexp = pp.Forward()
            sexp_list = pp.Forward()
            sexp_list = pp.Group(lp + pp.ZeroOrMore(sexp) + rp)
            sexp << (w | sexp_list)

            try:
                pr = sexp.parseString(schematic)
                print(pr)
            except pp.ParseException as e:
                print(e)

        except FileNotFoundError as exc:
            print("File {} not Found: {}".format(sch_file, exc))


if __name__ == '__main__':
    update_schematic(
        "RES-00000001", os.path.join(PROJECT_FOLDER, "test.kicad_sch"))
