
from io import StringIO
class Vertex(object):
	"""
	Represents a single vertex in a directed graph
	"""
	def __repr__(self):
		return "Vertex<{0}, {1}>".format(self.id, self.edges)

	def __init__(self, id, edges):
		self.id = id
		self.edges = edges


class Graph(object):
	"""
	Represents a directed graph
	"""
	def __repr__(self):
		return "Graph<{0}, {1}>".format(self.root,self.vertices)

	def __init__(self, root, vertices):
		self.root = root
		self.vertices = vertices

	def __print_dfs__(self, out: 'StringIO' , visited, cursor: 'Vertex'):
		if cursor.id in visited:
			return
		visited[cursor.id] = True
		for _, edge in cursor.edges.items():
			if edge.id in self.vertices :
				if cursor.id != '0':
					out.write("\t{0} -> {1}\n".format(cursor.id, edge.id))
				self.__print_dfs__(out,visited,edge)
		return

	def print(self, out: StringIO):
		self.__print_dfs__(out, {}, self.root)

def loads(input:str, root: str):
	lines = input.split("\n")
	vertex_map = {}
	for line in lines:
		from_to = line.split(',')
		if len(from_to) == 2:
			from_id = from_to[0]
			to_id = from_to[1]
			
			if from_id not in vertex_map:
				from_vertex = Vertex(from_id, edges={})
				vertex_map[from_id] = from_vertex
			else:
				from_vertex = vertex_map[from_id]
			
			
			if to_id not in vertex_map:
				to_vertex = Vertex(to_id, edges={})
				vertex_map[to_id] = to_vertex
			else:
				to_vertex = vertex_map[to_id]
			
			from_vertex.edges[to_id] = to_vertex
		else:
			raise Exception("Could not parse input line %s" % line)

	vertices = {}
	for k in vertex_map:
		vertices[k] = True
	if root not in vertex_map:
		raise Exception("root id %d is not in this graph" % root)

	root_vertex =  vertex_map[root]

	return Graph(root_vertex, vertices)
