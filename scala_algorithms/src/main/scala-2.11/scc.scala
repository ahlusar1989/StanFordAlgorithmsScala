/**
  * Created by saran on 10/15/16.
  */
object scc {

  def main(args: Array[String]) ={

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




  }

}
