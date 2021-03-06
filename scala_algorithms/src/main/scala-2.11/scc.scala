/**
  * Created by saran on 10/15/16.
  */
object scc {

  def main(args: Array[String]) = {
    /*
     * Kosaraju algorithm to find strongly connected components of a directed graph.
     */

    /** Vertex ID */
    type Id = Int

    case class Edge(tail: Id, head: Id) // a directed edge from tail to head

    case class Vertex(id: Id, edges: Set[Edge]) {
      def addEdge(edge: Edge) = this.copy(edges = this.edges + edge)

      def getAdjacent(reverse: Boolean): Set[Id] = {
        if (reverse) {
          // return all vertices with edges leading to this one
          edges.collect { case Edge(u, v) if v == id => u }
        } else {
          // return all vertices with edges leading from this one
          edges.collect { case Edge(u, v) if u == id => v }
        }
      }
    }

    case class Graph(vertices: Map[Id, Vertex]) {
      def apply(id: Id) = vertices(id)
    }

    /** Keeps track of when each node's DFS was finished */
    class FinishingTimeTracker(graph: Graph) {
      private[this] var finished: List[Id] = Nil

      def markFinished(vertex: Vertex): Unit = {
        // Add each vertex to the head as it finishes,
        // so we can easily iterate in reverse-finishing-time order
        finished = vertex.id :: finished
      }

      def getVerticesInReverseFinishingTimeOrder: Seq[Id] = finished
    }

    /** Keeps track of which nodes have been explored by DFS-Loop */
    class ExploredTracker {
      private[this] val explored = collection.mutable.Set[Id]()

      def markExplored(vertex: Vertex): Unit =
        explored += vertex.id
      def isExplored(vertex: Vertex) = explored contains vertex.id
    }

    /** Keeps track of the current leader node, and collects nodes into SCCs */
    trait LeaderRecorder {
      protected var sccs = Map[Id, Set[Id]]()
      private var currentLeader: Option[Id] = None

      def setCurrentLeader(vertex: Vertex): Unit =
        currentLeader = Some(vertex.id)

      def setLeaderFor(vertex: Vertex): Unit = {
        for (s <- currentLeader) {
          val scc = (sccs getOrElse(s, Set[Id]())) + vertex.id
          sccs = sccs + (s -> scc)
        }
      }
    }

    /** Tells us the size of the top N biggest SCCs */
    class SCCSizeCalculator extends LeaderRecorder {
      def getSccSizes(limit: Int): Seq[Int] = {
        sccs.values.view.map(_.size).toSeq.sorted.reverse.take(limit)
      }
    }

    /*
     * Build a graph from a list of directed edges
     */
    def buildGraph(input: Iterator[Array[Int]]): Graph = {
      val vertices = input.foldLeft(Map[Id,Vertex]()) {
        case (vertices, line) => {
          val edge = Edge(line(0), line(1))

          // Add the edge to both the head and tail vertices,
          // so that we can DFS the graph in reverse
          val tail = vertices.getOrElse(edge.tail, Vertex(edge.tail, Set[Edge]()))
          val head = vertices.getOrElse(edge.head, Vertex(edge.head, Set[Edge]()))

          vertices + (tail.id -> tail.addEdge(edge)) + (head.id -> head.addEdge(edge))
        }
      }
      Graph(vertices)
    }

    def dfs(graph: Graph,
            sourceVertex: Vertex,
            explored: ExploredTracker,
            finishingTimes: Option[FinishingTimeTracker],
            leaderRecorder: Option[LeaderRecorder],
            reverse: Boolean = false): Unit = {
      // Mark i as explored
      explored.markExplored(sourceVertex)

      // Set leader(i) := s
      for (lr <- leaderRecorder) {
        lr.setLeaderFor(sourceVertex)
      }

      // For each arc (i, j) in G
      for (id <- sourceVertex.getAdjacent(reverse)) {
        val j: Vertex = graph(id)
        // If j not yet explored
        if (!explored.isExplored(j)) {
          // DFS(G, j)
          dfs(graph, j, explored, finishingTimes, leaderRecorder, reverse)
        }
      }

      // Set f(i) := t
      for (ft <- finishingTimes) {
        ft.markFinished(sourceVertex)
      }
    }

    /** Runs DFS-Loop on a reversed version of the graph, collecting finishing times */
    def firstPass(graph: Graph): FinishingTimeTracker = {
      val finishingTimes = new FinishingTimeTracker(graph)
      val explored = new ExploredTracker()
      for (v <- graph.vertices.values) {
        if (!explored.isExplored(v)) {
          dfs(graph, v, explored, Some(finishingTimes), leaderRecorder=None, reverse=true)
        }
      }
      finishingTimes
    }

    /** Runs DFS-Loop on the graph, iterating nodes in reverse order of finishing time */
    def secondPass(graph: Graph, orderedVertices: Seq[Id]): Seq[Int] = {
      val sccSizeCalculator = new SCCSizeCalculator()
      val explored = new ExploredTracker()
      for (i <- orderedVertices) {
        val v = graph(i)
        if (!explored.isExplored(v)) {
          sccSizeCalculator.setCurrentLeader(v)
          dfs(graph, v, explored, finishingTimes=None, leaderRecorder=Some(sccSizeCalculator))
        }
      }
      sccSizeCalculator.getSccSizes(5)
    }

    val input: Iterator[Array[Int]] = {
      io.Source.fromFile(new java.io.File("/Users/saran/Desktop/Algorithms.txt"))
        .getLines
        .map(_.split(" ").map(_.toInt))
    }
    val graph = buildGraph(input)
    println(s"Built graph (${graph.vertices.size} nodes)")
    val orderedVertices = firstPass(graph).getVerticesInReverseFinishingTimeOrder
    println("Finished first pass")
    val sccSizes = secondPass(graph, orderedVertices)
    println("Finished second pass")
    println(sccSizes.mkString(","))


  }

}
