using NetMQ;
using NetMQ.Sockets;
using System;


namespace ZeroMQSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {
            using (var server = new PublisherSocket("@tcp://localhost:8080")) // bind
            {

                while (true)
                {
                    // Send a response back from the server
                    server.SendFrame("test");

                    Thread.Sleep(1000);
                }
  


            }
        }
    }
}
