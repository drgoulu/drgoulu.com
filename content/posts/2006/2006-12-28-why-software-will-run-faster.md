---
title: "Why Software Will Run Faster"
date: 2006-12-28
categories: 
  - "cat2"
tags: 
  - "futur"
  - "informatique"
---

in "[Why Software Won't Run Any Faster Any Time Soon](http://worldcadaccess.typepad.com/blog/2006/12/why_software_wo.html)", Ralph Gabowski quotes 7 facts that look correct, but I think his conclusion isn't.

Multicore (fact 3) is a hardware solution to implement multiprocessing at a "medium grain" level : it is efficient to run different programs, or processes, or threads that have little communication with others (to avoid problem mentioned in fact 5).

However, there is no reason to "rewrite software for multicore" (fact 4). Compilers will soon integrate tools like [Intel's Threading Tools](http://software.intel.com/en-us/intel-sdp-home/) to generate optimized multithreaded code, perhaps with a little help from human preprocessing (with [OpenMP](http://openmp.org/wp/) for example).

The reason why I'm confident about this is that compilers already handle very well "fine grain" parallelism, or "vectorization", to execute independent operations (almost) simultaneously.

GPUs are precisely "fine grain parallel" processors that were designed for graphics (fact 7), but this might change. Analysts think the purchase of ATI by AMD annouces a merge of CPUs and GPUs in the near future. We will likely see soon multicores CPUs with highly parallelized cores, each being able to work either as a GPU or as a CPU on demand. The [Cell processor from IBM](http://www.research.ibm.com/cell/), used in Sony's Playstation 3 might be considered as a first attempt in this direction. And true, few software can take advantage of its power for now.

The fact that CPU clock speeds "stalled" (fact 1) doesn't mean that processing power did so. Parallelism is a way to continue to increase Flops (FLoating Point Operations per Second) without increase in Gigaherz, which proved to be a "cheap", non-innovative way to improve performance.

Finally, 64 bits processors bring indeed the power to address gigantic memory (fact 6) which looks almost useless at first sight. However, every programmer knows the tradeoff between cpu and memory : you can either store large tables of data and access it fast, or spend time to recalculate the data you need when you need it. So with larger, faster and cheaper memory, a good way to make software faster is to store more temporary data in huge caches.

One step further is to consider that a 64 bits address space is (much) larger than any hard disk array in the world. So why constinue to distinguish hard disk storage and RAM memory ? Some experimental "persistent" operating systems handle the whole hard disk as a swap file for a large virtual memory which could contain all the data on your computer, eliminating the need for "files".

Finally, "large grain" parallelism could be used to distribute work across computers in a network. Some animation rendering and research-oriented screensavers already work that way. Now imagine this combined with a "persistent" OS as mentioned above. Think about a network of multi-core vectorized processors sharing the _same_ address space, each computer using disk stoarge only as a cache between the processor and the network.

This is not sci-fi. It is called a "single address space operating system" (sasos), and several functional prototypes exist. Among them, [Opal](http://www.cs.washington.edu/homes/levy/opal/opal.html) mentions CAD/CAM explicitely as a potential application. Imagine users of such a package sharing the very same model directly in memory: they will never need to copy any file, to rebuild a part, never load, never check in or check-out. Imagine the improvement in performance when a software doesn't have to do anything twice...

In the shorter term, Vista will be slower than XP on a single core machine (fact 2). It might be slower on a dual-core. But it should be faster on a quad-core, unless Microsoft bloated it with so many "features" that it leaves only 1 core for applications ...
