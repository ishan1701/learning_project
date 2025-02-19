A trigger is kind of hook to start a workflow to start

A basic example of trigger is 
When a pr is creation for a master branch

```
name: Trigger
on:
   pull_request:
     branch : [master]
```


Below are triggers which can be used
1. Manual triggers (workflow_dispatch)

This will allow to run the workflow manually via the UI.
```
on:
  workflow_dispatch:
    inputs:
      environment:
        description: "Select environment"
        required: true
        type: choice
        options: [staging, production]
```

2. code events( push, pull_request)
```
on:
  push:
    branches:
      - main

```

3. schedule
4. repo events
5. ci/cd workflows