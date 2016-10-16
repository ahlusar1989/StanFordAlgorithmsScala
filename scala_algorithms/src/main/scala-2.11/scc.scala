/**
  * Created by saran on 10/15/16.
  */
object scc {

  def main(args: Array[String]) = {

  type Id = Int

    case class Edge(tail: Id, head:Id) //a directed edge from head to tail

    case class Vertex(id: Id, edges: Set[Edge]){
      def addEdge(edge: Edge) = this.copy(edges = this.edges + edge)

      def getAdjacentEdge(reverse:Boolean): Set[Id] = {
        if(reverse){
          edges.collect{case Edge(u,v) if v == id => u }
        }else{
          edges.collect{case Edge(u,v) if u == id => v }
        }
      }

    }

    case class Graph(vertices: Map[Id, Vertex]){
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

    val input: Iterator[Array[Int]] = {
      io.Source.fromFile(new java.io.File("/Users/saran/Desktop/Algorithms/SCC.txt"))
        .getLines
        .map(_.split(" ").map(_.toInt))
    }
    val graph = buildGraph(input)
    println(s"Built graph (${graph.vertices.size} nodes)")


  }

}
