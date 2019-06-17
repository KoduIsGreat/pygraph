from pygraph import graph
import io

def sort_by_new_line(input: str):
    sa = input.split('\n')
    return "\n".join(sorted(sa))


def test_una():
	test_in = """0,307562200
0,307578700
0,307601400
0,307635600
0,307668700
0,307676500
307562200,307586600
307578700,307586600
307586600,307586700
307586700,307586800
307586800,307592300
307601400,307586800"""

	expected_out = """
	307562200 -> 307586600
	307578700 -> 307586600
	307586600 -> 307586700
	307586700 -> 307586800
	307586800 -> 307592300
	307601400 -> 307586800"""

	g = graph.loads(test_in, '0')
	out = io.StringIO("")
	g.print(out)
	out = sort_by_new_line(out.getvalue())
	assert out == expected_out, "\n got:\n {0} \n\n wanted:\n {1} ".format(out,expected_out)
