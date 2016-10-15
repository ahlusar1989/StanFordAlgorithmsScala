/**
  * Created by saran on 10/15/16.
  */
object scc {

  def main(args: Array[String]): Unit ={

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







  }

}
