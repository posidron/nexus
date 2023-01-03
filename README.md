# Install

```shell
pipenv install
pipenv run pyinstaller nexus.py --onefile
mv dist/nexus /usr/local/bin/
```

# Run

```bash
export OPENAI_ACCESS_TOKEN=token # https://beta.openai.com/account/api-keys
```

```bash
nexus "create a fib sequence in python" | nexus "convert it to javascript"
```

```javascript
//define a function to create the Fibonacci Sequence
function FibonacciSequence(n) {
    // start with the first two terms
    let a = 0; // first term
    let b = 1; // second term
    // check to make sure the desired number is at least 2
    if (n < 2) {
        return a;
    } else {
        // use a for loop to create the Fibonacci sequence
        for(let i = 2; i < n; i++) {
            let c = a + b; // next term
            a = b;
            b = c;
        }
        return b;
    }
}

// define the number to generate in the Fibonacci sequence
let n = 14;
// display the result
console.log(FibonacciSequence(n)); // result = 233
```

```bash
w | nexus "format to json"
```

```json
{
  "time": "1:06",
  "up_days": "7 days",
  "load_averages": "3.67 4.40 4.85",
  "users": [
    {
      "user": "posidron",
      "tty": "console",
      "from": "-",
      "login": "26Dec22",
      "idle": "7days",
      "what": "-"
    },
    {
      "user": "posidron",
      "tty": "s000",
      "from": "-",
      "login": "Mon23",
      "idle": "",
      "what": "fish (figterm)"
    },
  ]
}
```

```bash
nexus "is 2023 prime?"
```

```
No, 2023 is not a prime number. It is a composite number made up of the factors 2, 7, 11, and 13.
```

```bash
nexus "create an azure arm template for deplying a docker container"
```

```json
{
    "$schema": "https://schema.management.azure.com/schemas/2015-01-01/deploymentTemplate.json#",
    "contentVersion": "1.0.0.0",
    "parameters": {
        "containerName": {
            "type": "string"
        },
        "dockerImage": {
            "type": "string"
        },
        "containerPort": {
            "type": "string"
        },
        "hostPort": {
            "type": "string"
        }
    },
    "resources": [
        {
            "type": "Microsoft.Compute/virtualMachines/extensions",
            "name": "[concat(parameters('containerName'),'/DockerExtension')]",
            "apiVersion": "2015-05-01-preview",
            "location": "[resourceGroup().location]",
            "dependsOn": [
                "[concat('Microsoft.Compute/virtualMachines/', parameters('containerName'))]"
            ],
            "properties": {
                "publisher": "Microsoft.Azure.Extensions",
                "type": "CustomScript",
                "typeHandlerVersion": "2.0",
                "autoUpgradeMinorVersion": true,
                "settings": {
                    "fileUris": [
                        "https://raw.githubusercontent.com/azurearmuser/docker/master/docker-installer.sh"
                    ],
                    "commandToExecute": "[concat('bash docker-installer.sh ', parameters('dockerImage'), ' ', parameters('containerPort'), ' ', parameters('hostPort'))]"
                }
            }
        }
    ],
    "outputs": {}
}
```


```bash
cat vuln.cc | nexus "identify the vulnerability"
```

```cpp
int main(int argc, char **argv) {
  int *array = new int[100];
  array[0] = 0;
  int res = array[argc + 100];
  delete [] array;
  return res;
}
```

```
The vulnerability in this code is a buffer overflow, which is caused by accessing an array element
with an index of argc + 100, which is outside the bounds of array. This can lead to memory
corruption and potentially a crash or intrusion.
```
