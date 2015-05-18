---
title: The PanDA System
description: Distributed workload management system for production and analysis
author: Torre Wenaus
layout: page
---

The PanDA Production ANd Distributed Analysis system is designed to meet the demanding computing requirements of the ATLAS Experiment at the LHC. The extreme data-intensive computing needs of ATLAS require a highly scalable and flexible data-driven workload management system serving both production and distributed analysis processing. ATLAS processing places challenging requirements on throughput, scalability, robustness, efficient resource utilization, minimal operations manpower, constant adaptation to new workflows and use cases, and not least, tight integration of data management with processing workflow.

While PanDA was initially designed first and foremost for ATLAS, the capability it provides for very large scale data-intensive distributed computing is becoming increasingly important across computational science fields, which motivated the [BigPanDA project](/bigpanda.html) to extend PanDA's applicability beyond ATLAS.

PanDA harvests and exploits processing resources through autonomous pilot jobs launching in job slots and requesting to a central PanDA service for the dispatch of work. The PanDA server manages a coherent global queue of production and analysis work to be performed, and allocates work to requesting pilots based on intelligent brokerage and the characteristics of the resource. PanDA was initially developed for US based ATLAS production and analysis, and assumed that role in late 2005. In October 2007 PanDA was adopted by the ATLAS Collaboration as the sole system for distributed processing production across the Collaboration. It proved itself as a scalable and reliable system capable of handling very large workflow. In 2008 it was adopted by ATLAS for user analysis processing as well. The BigPanDA project extending PanDA beyond ATLAS began in 2012.

PanDA throughput has been rising continuously over the years, with the system showing excellent scalability. In 2009, a typical PanDA processing rate was 50k jobs/day and 14k CPU wall-time hours/day for production at 100 sites around the world, and 3-5k jobs/day for analysis. In 2015, PanDA processes close to a million jobs per day, with about 150k jobs running at any given time, peaking at about 200k. The PanDA analysis user community numbers over 1400. ATLAS PanDA processes more than an Exabyte of data each year. The system is expected to easily meet the growing needs over the next decade, albeit not without change and evolution, in the back end databases for example. PanDA evolution is continuous in order to cope with evolving requirements and use cases.

See the [PanDA twiki](https://twiki.cern.ch/twiki/bin/view/PanDA/PanDA) for details on PanDA and its components.

## PanDA architecture

The core components of PanDA are as follows.

### PanDA server

The PanDA server is the central PanDA hub composed of several components that make up the core of PanDA. It is implemented as a stateless REST web service over Apache mod_python (PanDA is written in python) and with an Oracle or MySQL back end. The server manages the global job queue, keeping track of all active jobs in the system. 
It presents APIs by which clients inject tasks and jobs into PanDA, and receive status information.
It brokers work to processing resources, matching job attributes with site and pilot attributes. It manages the dispatch of input data to processing sites, and implements data pre-placement requirements. It receives requests for work from pilots and dispatches jobs matching the capabilities of the site and worker node (data availability, disk space, memory etc.) It manages heartbeat and other status information coming from pilots.

PanDA, as a workload manager for data-intensive processing, manages data flow and access as well as processing, and the PanDA server provides the data management services required (dataset management, data dispatch to and retrieval from sites, brokering jobs to non-local but 'nearby' data in network terms, etc.)

See the [PanDA server twiki](https://twiki.cern.ch/twiki/bin/view/PanDA/PandaServer) for more information.

### PanDA pilot

The PanDA pilot is the execution environment, effectively a wrapper, for PanDA jobs. Pilots request and receive job payloads from the PanDA server's dispatcher, perform setup and cleanup work surrounding the job, and run the jobs themselves, regularly reporting status to PanDA during execution. The pilot manages and encapsulates the heterogeneity and complexity of PanDA's operating environments and application payloads. Consequently while the pilot is conceptually simple, in reality it is a highly complex piece of software. Major recent extensions include support for HPCs, the Event Service, and object stores.

The pilot is detailed in the [pilot twiki](https://twiki.cern.ch/twiki/bin/view/PanDA/PandaPilot). Pilot release history is recorded in the [pilot blog](http://pandapilotblog.blogspot.com/).

### PanDA monitor

The PanDA monitor is the web based portal into PanDA that is used by end users and experts as the window into PanDA's operation. It provides information from high level summaries of system activity and performance down to detailed drill-down information on jobs and their failure modes. It allows analysis users to monitor their tasks in the system, site responsibles to monitor the activity and performance of their site, and production operators to monitor the global throughput of tasks.

The ATLAS instance of the PanDA monitor can be found [here](http://bigpanda.cern.ch).

### Pilot factories

PanDA is agnostic as to how the pilots asking for work are created and managed, and in fact ATLAS has never had just one mechanism for provisioning pilots, not least because the heterogeneity of the platforms PanDA can use make a single mechanism for harnessing resources from them unrealistic. While obviously essential to PanDA's functioning, pilot provisioning mechanisms are not part of PanDA proper.
Provisioning is generally provided by pilot factories, though some resources take other approaches (NorduGrid, HPCs, ATLAS@Home).

The most widely used tools for pilot management are [AutoPyFactory](http://iopscience.iop.org/1742-6596/396/3/032016) and [ARC Control Tower](http://iopscience.iop.org/1742-6596/331/7/072013).

## New developments

The PanDA team took the opportunity of the 2013-2014 LHC Long Shutdown to implement many new developments, highlighted by the following.

### JEDI

A major extension to PanDA was implemented during 2013-2014, the Job Execution and Definition Interface (JEDI). JEDI is an intelligent component in the panda server capable of task-level workload management. JEDI takes high level descriptions of work to be performed, in the form of tasks, and dynamically partitions them for processing in an optimal manner given PanDA's knowledge of the processing resources available. Work can be partitioned down to fine event-level granularity if desired; this capability is used in the Event Service. JEDI is designed to work with the DEFT task definition interface; the two components DEFT and JEDI constitute Prodsys2, the new ATLAS production system implemented for Run 2. JEDI is currently only used by ATLAS but is experiment-neutral.

With the advent of JEDI, PanDA's workflow management underwent a fundamental change. Whereas formerly PanDA accepted work in terms of jobs, had little flexibility in the structure of those jobs, and defined its task in terms of completing those jobs, with JEDI the workflow is different. It is now task oriented, where tasks are high level work assignments mapping more directly to the requests of physicist users: process these inputs through these transformations to produce those outputs. And PanDA's objective and metric for completing tasks is now the successful processing of input files (and their constituent events), not processing jobs. Jobs are a fluid implementation detail of the workflow. The change not only makes PanDA a more powerful and flexible engine for production workloads, it also serves user analysis much better, allowing users to submit and track work at the task level.

JEDI details are in the [JEDI twiki](https://twiki.cern.ch/twiki/bin/view/PanDA/PandaJEDI).

### Event Service

By the start of Run 2 in Spring 2015, the ATLAS experiment \cite{atlaspaper} had accumulated to date a globally distributed data volume in excess of 160 Petabytes, processed at a scale of about 4M CPU-hours/day at about 140 computing centers around the world. Even with this massive processing scale the experiment is resource limited, and the future will be even more constraining: upgrades over the next decade will bring an order of magnitude increase in computing requirements. For these reasons, making full and efficient use of all available processing resources is essential.

Opportunistic processing resources have a large potential for expanding the ATLAS processing pool. High performance supercomputers (HPCs), cost-effective clouds such as the Amazon spot market, volunteer computing (ATLAS@Home), and shared grid resources are all promising sources. On such resources slot lifetime is unpredictable, variable and may be very short (or very long); exploiting them well requires adapting to this characteristic. A new fine grained approach to event processing, the ATLAS Event Service, is designed to do so.

The ATLAS Event Service (ES) is designed to open opportunistic resources to efficient utilization, and to improve overall efficiency in the utilization of processing and storage. The ES implements quasi-continuous event streaming through worker nodes, enabling full and efficient exploitation through their lifetime whether that is 30 minutes, 30 hours, or 30 seconds from now, with no advance notice. The ES achieves this by decoupling processing from the chunkiness of files, streaming events into a worker and streaming the outputs away in a quasi-continuous manner, with a tunable granularity typically set to 15 minutes or so. While the worker persists, it will elastically continue to consume events and stream away outputs with no need to tailor workload execution time to resource lifetime. When the worker terminates for whatever reason, losses are limited to the last few minutes, corresponding to a single event when the task is ATLAS Monte Carlo simulation. The approach offers the efficiency and scheduling flexibility of preemption without the application needing to support or utilize checkpointing.

In its workflow aspects the Event Service builds principally on PanDA, JEDI and ATLAS's parallel offline framework, athenaMP. PanDA and JEDI manage the workflows in a fully automatic way, from high level task specifications defined by physicists through partitioning and executing the work on dynamically selected resources, merging results, and chaining subsequent downstream processing. The payloads launched by PanDA for the ES are instances of AthenaMP; its parallel capabilities are used to manage the distribution and processing of events concurrently among parallel workers.

In its dataflow aspects the Event Service relies on the ATLAS event I/O system's support for efficient WAN data access, the uniform support for xrootd based remote data access across ATLAS, highly scalable object stores for data storage that architecturally match the fine grained data flows, and the excellent high performance networking fabric on which the success of LHC computing has long been built. 

A specialization of the Event Service for HPCs, Yoda, was developed to accommodate the particular features of HPC architectures, most notably the lack of outbound access from worker nodes. Yoda is a miniaturization of the PanDA/JEDI event workflow management to operate within the HPC itself, with MPI replacing HTTP communication. Yoda's master/client architecture allows tailoring of workloads automatically and dynamically to whatever scheduling opportunities the resource presents, like sand filling up a "full" jar of rocks. 

The present and near term use case for the Event Service is in Monte Carlo simulation, the single largest consumer of CPU in ATLAS at about half of all processing resources. MC is a relatively simple, CPU-intensive payload that is amenable to operating on HPCs. Event Service based simulation is operating on several opportunistic platforms, and will begin production operation in Spring 2015. The system is close to entering production on HPC, commercial cloud, grid and volunteer computing platforms. 

More information on the Event Service is in the [Event Service twiki](https://twiki.cern.ch/twiki/bin/view/PanDA/EventServer). See also the CHEP 2015 presentations and proceedings papers linked from the [publications page](pubs.html).

### BigPanDA monitor

One of the objectives of the BigPanDA project was to provide high quality, experiment neutral and extensible monitoring and visualization of PanDA operation. This was realized in a new implementation of the PanDA monitor, the BigPanDA monitor, that has now replaced the old. It uses django to isolate database interfacing and data preparation from presentation views. It underwent large expansions in scope in order to support task based monitoring required by JEDI and the new production system. It supports both the Oracle and MySQL database back ends of PanDA. It is now being extended to improve its performance and interactivity, with internal caching (e.g. Redis) and client side functionality (javascript operating on json data from the server).

The BigPanDA monitor ATLAS instance is [here](http://bigpanda.cern.ch).

### Modularization and packaging

In an ongoing program of work, all PanDA components have been undergoing refactoring and modularization, isolating their ATLAS dependencies and making it possible for other experiments to begin with an experiment-neutral PanDA and tailor it to their needs through experiment specific modules. Improving the packaging has also been an important activity, in-house and in collaboration with software packaging and deployment experts in the [Open Science Grid (OSG)](http://opensciencegrid.org).

## PanDA Project Support

US ATLAS has supported PanDA development since PanDA's inception in 2005.

DOE ASCR and DOE HEP funded the proposal "A next generation workload management and analysis system for big data", beginning in 2012, with lead PIs Alexei Klimentov (BNL) and Kaushik De (UTA).

* [US ATLAS](http://www.usatlas.bnl.gov/)
* [DOE ASCR](http://science.energy.gov/ascr/)
* [DOE HEP](http://science.energy.gov/hep/)
