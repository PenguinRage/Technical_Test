### Cloud Computing Theory

##### What is the difference between container based virtualization and hypervisor based virtualisation?

The main difference between container based virtualisation and hypervisor based virtualisation is that the hypervisor based operates on a hardware level and the container based operates on a operating system level. 

In hypervisor virtualization,  a thin base layer is used to redirect all instructions coming from virtual machines to the underlying hardware layer. This base layer is a thin kernel with virtualization features onboard. This is used to emulate the underlying physical hardware and create virtual hardware(with your desired resources like processor and memory). And on top of these newly created virtual hardware an operating system is installed. The hardware running the hypervisor is called the host operating system where as all emulated machines  running inside them are referred to as guest operating systems.
  
Container-based virtualisation utilises kernel features to create an isolated environment for processes. In contrast to the hypervisor-based virtualisation, containers do not get their own virtualised hardware of the host system. The basic idea of container-based virtualization is to run a kernel, with several different virtual machines installed on top of it. In contrast to hypervisor-based virtualization, a virtual machine is not a complete operating system instance, but rather a partial instance of the operating system that works in a smart way with the virtualization layer in the host operating system kernel. 

##### In Amazon Web Services, explain the difference between a **Region**, **Availability Zone** & **Instance** in relation to fault domains.

In general, a fault domain is essentially a rack of servers. It consumes subsystems like network, power, cooling etc. 

An EC2 instance is a virtual server in Amazon's Elastic Compute Cloud (EC2) for running applications on the Amazon Web Services (AWS) infrastructure, each instance is hosted within a Region and an Availability Zone. Amazon EC2 is hosted in multiple locations world-wide. These locations are composed of regions and Availability Zones. Each region is a separate geographic area. Each region has multiple, isolated locations known as Availability Zones. Each Amazon EC2 region is designed to be completely isolated from the other Amazon EC2 regions. This achieves the greatest possible fault tolerance and stability. Each Availability Zone is isolated, but the Availability Zones in a region are connected through low-latency links. When you launch an instance, you can select an Availability Zone. If you distribute your instances across multiple Availability Zones and one instance fails, you can design your application so that an instance in another Availability Zone can handle requests.
