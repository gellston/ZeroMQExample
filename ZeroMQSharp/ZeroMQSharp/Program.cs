using NetMQ;
using NetMQ.Sockets;
using Newtonsoft.Json;
using System;
using System.Net;
using System.Net.WebSockets;
using System.Text;
using System.Text.Json.Serialization;
using ZeroMQSharp.Message;


namespace ZeroMQSharp
{
    internal class Program
    {
        static void Main(string[] args)
        {

            using SubscriberSocket subscriber= new SubscriberSocket();
            subscriber.Connect("tcp://localhost:9090");
            subscriber.Subscribe("");
            using NetMQPoller poller = new NetMQPoller { subscriber };
            subscriber.ReceiveReady += (s, arg) =>
            {
                string msg = arg.Socket.ReceiveFrameString();
                System.Console.WriteLine(msg);

            };

            poller.Run();

            System.Diagnostics.Debug.WriteLine("test");

        }
    }
}
