import math

class Graph:
    def __init__(self):
        #another way to implement graph example = {a:{b:5,c:9}, c:{a:9,e:3}}
        self.v = []
        self.matrix = []

    def add_vertex(self, label):
        '''add a vertex with the specified label. 
        Return the graph. 
        label must be a string or raise ValueError
        '''
        if not isinstance(label, str):
            raise ValueError
        self.v.append(label)
        # expand matrix
        for lyst in self.matrix:
            lyst.append(math.inf) # add column
        self.matrix.append([]) # add row
        width = len(self.v)
        for i in range(width):
            self.matrix[-1].append(math.inf)
        return Graph()

    def add_edge(self, src, dest, w):
        '''add an edge from vertex src to vertex dest with weight w. 
        Return the graph. 
        validate src, dest, and w: raise ValueError if not valid.
        '''
        #validate
        w = float(w)
        start = self.v.index(src)
        end = self.v.index(dest)
        self.matrix[start][end] = w
        return Graph()

    def get_weight(self, src, dest):
        '''Return the weight on edge src-dest
        (math.inf if no path exists, raise ValueError if src or dest not added to graph).
        '''
        #validate
        start = self.v.index(src)
        end = self.v.index(dest)
        return self.matrix[start][end]

    def dfs(self, starting_vertex):
        '''Return a generator for traversing the graph in 
        depth-first order starting from the specified vertex. 
        Raise a ValueError if the vertex does not exist.
        '''
        span = []
        stack = []
        stack.append(starting_vertex)
        span.append(starting_vertex)
        def visit(vert):
            start = self.v.index(vert)
            last_nei = None
            ind = -1
            for item in self.matrix[start]:
                ind += 1
                if item < math.inf and self.v[ind] not in span:
                    last_nei = self.v[ind]
            if last_nei is None:
                stack.pop()
            else:
                span.append(last_nei)
                stack.append(last_nei)
                visit(last_nei)
            if not stack:
                return
            visit(stack[-1])
        visit(starting_vertex)
        return span

    def bfs(self, starting_vertex):
        '''Return a generator for traversing the graph in
        breadth-first order starting from the specified vertex.
        Raise a ValueError if the vertex does not exist.
        '''
        span = []
        all_nei = []
        all_nei.append(starting_vertex)
        while all_nei:
            current = all_nei[0]
            start = self.v.index(current) #will raise the value error
            ind = -1
            span.append(current)
            for item in self.matrix[start]:
                ind += 1
                if item < math.inf and self.v[ind] not in span and self.v[ind] not in all_nei:
                    all_nei.append(self.v[ind])
            all_nei.pop(0)
        return span

    def dsp(self, src, dest):
        '''Return a tuple (path length, the list of vertices on the path from dest back to src).
        If no path exists, return the tuple (math.inf, empty list.)
        '''
        #I was going to solve this with the dsp_all() dictionary but had the code so I left it
        start = self.v.index(src) #index of start vertex
        goal = self.v.index(dest) #index of end vertex
        ans = [] #answer will be appended to this list
        d = [] # list of weights
        p = [] # list of indicies of vertices
        lyst = [] # all vertices that can be reached from starting vertex
        reached = set({}) #set of vertices already visited
        ind = -1
        #step 1
        for w in self.matrix[start]:
            ind += 1
            d.append(w)
            if w < math.inf:
                p.append(start)
                lyst.append(self.v[ind])
            else:
                p.append(0)
        reached.add(src)
        while lyst: #step 2
            #step 3
            least = math.inf
            for vert in lyst:
                ind = self.v.index(vert)
                if d[ind] < least:
                    vind = ind
                    least = d[ind]
            lyst.remove(self.v[vind])
            reached.add(self.v[vind])
            #step 4
            ind = -1
            for edge in self.matrix[vind]:
                ind += 1
                if edge < math.inf and self.v[ind] not in reached:
                    #if d[ind] changes, set p[ind] = vind, add v[ind] to lyst
                    the_min = min(d[ind], d[vind] + self.matrix[vind][ind])
                    if the_min != d[ind]:
                        p[ind] = vind
                        if self.v[ind] not in lyst:
                            lyst.append(self.v[ind])
                    d[ind] = the_min
        #create answer tuple
        ans.append(d[goal])
        ind = p[goal]
        path = []
        if d[goal] < math.inf:
            path.append(dest)
            while ind != start:
                path.append(self.v[ind])
                ind = p[ind]
            path.append(src)
        ans.append(path[::-1])
        return tuple(ans)

    def dsp_all(self, src):
        '''Return a dictionary of the shortest weighted path between src 
        and all other vertices using Dijkstra's Shortest Path algorithm. 
        In the dictionary, the key is the the destination vertex label, 
        the value is a list of vertices on the path from src to dest inclusive.
        '''
        start = self.v.index(src) #index of start vertex
        ans = {} #answer will be appended to this dictionary
        d = [] # list of weights
        p = [] # list of indicies of vertices
        lyst = [] # all vertices that can be reached from starting vertex
        reached = set() #set of vertices already visited
        ind = -1
        #step 1
        for w in self.matrix[start]:
            ind += 1
            d.append(w)
            if w < math.inf:
                p.append(start)
                lyst.append(self.v[ind])
            else:
                p.append(0)
        reached.add(src)
        while lyst: #step 2
            #step 3
            least = math.inf
            for vert in lyst:
                ind = self.v.index(vert)
                if d[ind] < least:
                    vind = ind
                    least = d[ind]
            lyst.remove(self.v[vind])
            reached.add(self.v[vind])
            #step 4
            ind = -1
            for edge in self.matrix[vind]:
                ind += 1
                if edge < math.inf and self.v[ind] not in reached:
                    #if d[ind] changes, set p[ind] = vind, add v[ind] to lyst
                    the_min = min(d[ind], d[vind] + self.matrix[vind][ind])
                    if the_min != d[ind]:
                        p[ind] = vind
                        if self.v[ind] not in lyst:
                            lyst.append(self.v[ind])
                    d[ind] = the_min
        #create answer dictionary
        for dest in self.v:
            goal = self.v.index(dest) #index of end vertex
            ind = p[goal]
            path = []
            if d[goal] < math.inf:
                path.append(dest)
                while ind != start:
                    path.append(self.v[ind])
                    ind = p[ind]
                path.append(src)
            if not path and dest == src:
                path.append(src)
            ans[dest] = path[::-1]
        return ans

    def __str__(self):
        '''Produce a string representation of the graph that can be used with print(). 
        The format of the graph should be in GraphViz dot notation
        '''
        print_list = []
        start_vert = -1
        for lyst in self.matrix:
            end_vert = -1
            start_vert += 1
            for item in lyst:
                end_vert += 1
                if item != math.inf:
                    print_list.append(f'   {self.v[start_vert]} -> {self.v[end_vert]} [label="{item}",weight="{item}"];')
        a = '\n'.join(print_list)
        return f"digraph G {{\n{a}\n}}\n"

def main():
    # 1.Construct the graph shown in Figure 1 using your ADT.
    g = Graph()
    g.add_vertex("A")
    g.add_vertex("B")
    g.add_vertex("C")
    g.add_vertex("D")
    g.add_vertex("E")
    g.add_vertex("F")
    g.add_edge("A", "B", 2)
    g.add_edge("A", "F", 9)
    g.add_edge("B", "C", 8)
    g.add_edge("B", "D", 15)
    g.add_edge("B", "F", 6)
    g.add_edge("C", "D", 1)
    g.add_edge("E", "C", 7)
    g.add_edge("E", "D", 3)
    g.add_edge("F", "B", 6)
    g.add_edge("F", "E", 3)
    # 2.Print it to the console in GraphViz notation as shown in Figure 1. 
    print(g)
    # 3.Print results of DFS starting with vertex “A” as shown in Figure 2.
    print("starting DFS with vertex A")
    for vertex in g.dfs("A"):
        print(vertex, end = "")
    print('\n')
    # 4.BFS starting with vertex “A” as shown in Figure 3. 
    print("starting BFS with vertex A")
    for vertex in g.bfs("A"):
        print(vertex, end = "")
    print('\n')
    # 5.Print the path from vertex “ A” to vertex “F” (not shown here) using Djikstra’s shortest path algorithm (DSP) as a string like #3 and #4.
    af = g.dsp("A", "F")
    print("starting DSP from vertex A to F")
    for vertex in af[1]:
        print(vertex, end = "")
    print('\n')
    # 6.Print the shortest paths from “A” to each other vertex, one path per line using DSP.
    a_all = g.dsp_all("A")
    print("DSP from vertex A to all of vertices")
    for key in a_all:
        for val in a_all[key]:
            print(val, end = "")
        print('\n')

if __name__ == "__main__":
    main()