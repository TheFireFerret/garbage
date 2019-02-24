Look at rule 58. The action sensor is what you use below as the action

```
{  "name":"Movie Mode Disable",
   "conditions":[
        {"address":"/lights/12/state/on","operator":"eq","value":"true"},
        {"address":"/lights/13/state/on","operator":"eq","value":"false"}
   ],
   "actions":[	
              {"address":"/sensors/79/config","method":"PUT","body":{"on":false}}
]}


{  "name":"Movie Mode Disable 2",
   "conditions":[
        {"address":"/lights/12/state/on","operator":"eq","value":"false"},
        {"address":"/lights/13/state/on","operator":"eq","value":"true"}
   ],
   "actions":[	
              {"address":"/sensors/79/config","method":"PUT","body":{"on":false}}
]}


{  "name":"Movie Mode Enable",
   "conditions":[
        {"address":"/lights/12/state/on","operator":"eq","value":"true"},
        {"address":"/lights/13/state/on","operator":"eq","value":"true"}
   ],
   "actions":[	
              {"address":"/sensors/79/config","method":"PUT","body":{"on":true}}
]}


{  "name":"Movie Mode Enable 2",
   "conditions":[
        {"address":"/lights/12/state/on","operator":"eq","value":"false"},
        {"address":"/lights/13/state/on","operator":"eq","value":"false"}
   ],
   "actions":[	
              {"address":"/sensors/79/config","method":"PUT","body":{"on":true}}
]}
```
