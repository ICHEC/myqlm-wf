# myqlm Workflows

This repository contains various examples of hybrid quantum-classical workflows.

## Workflow 1

This is the simplest workflow. The example is in folder [workflow1](./workflow1/), and the workflow looks like following -

```mermaid
graph LR
a((Init)) --> b>"Quantum
Job"] --> c>"Classical
Job"]-->e((End))

style b fill:#ffcccc
style c fill:#ccffcc
```

## Workflow 2

This example shows how to taskfarm quantum-classical jobs as above in `workflow1` via MPI. This example is in folder [workflow2](./workflow2/) and looks like following - 


```mermaid
graph LR
a((Init))
subgraph Tasks
b1>"Quantum Job 1"]
b2>"Quantum Job 2"]
b3>"Quantum Job 3"]
b4>"Quantum Job ..."]
c1>"Classical Job 1"]
c2>"Classical Job 2"]
c3>"Classical Job 3"]
c4>"Classical Job ..."]
end
e((Collect)) --> f((End))

a--parameters--> b1 & b2 & b3 & b4
b1 --statevector 1--> c1
b2 --statevector 2--> c2
b3 --statevector 3--> c3
b4 --statevector ..--> c4
c1 & c2 & c3 & c4 --Results--> e

style b1 fill:#ffcccc
style b2 fill:#ffcccc
style b3 fill:#ffcccc
style b4 fill:#ffcccc

style c1 fill:#ccffcc
style c2 fill:#ccffcc
style c3 fill:#ccffcc
style c4 fill:#ccffcc
```

### Dependency

The only dependency to execute the codes is [myqlm](https://myqlm.github.io/) package, preferably in a conda like environment, and setup for remote QPU of myqlm.

For any queries, contact - rajarshi.tiwari @ ichec.ie.

### Acknlowedgement

This activity is part of the HPCQS project, and work is done under the WP3-WP5 coordination where ICHEC and ParTec are partners.