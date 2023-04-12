# Vagrant Primer

You will be using a Vagrant box during your development cycle and as part of your onboarding, we would like to introduce
you to Vagrant, a powerful virtualization tool. This primer will provide you with an overview of Vagrant boxes and
how they are used within our development environment.

Vagrant is an open-source tool that simplifies the process of setting up and managing virtual machines (VMs).
Vagrant boxes are pre-packaged VM templates that can be easily shared and customized. By using Vagrant boxes,
we can create consistent, reproducible development environments for our projects, making it easier for developers to
collaborate and contribute effectively.

### Basic Vagrant Commands
Here is a list of basic Vagrant commands to help you get started with managing your Vagrant environments:

1. **vagrant init**: Initializes a new Vagrant environment by creating a Vagrantfile in the current directory. 
You can optionally specify a box name and URL to preconfigure the Vagrantfile.

```
vagrant init [box_name] [box_url]
```

2. **vagrant up**: Starts and provisions the Vagrant environment according to the Vagrantfile in the current directory.

```
vagrant up
```

3. **vagrant halt**: Shuts down the running Vagrant environment.

```
vagrant halt
```

4. **vagrant reload**: Restarts the Vagrant environment, applying any changes made to the Vagrantfile since the last vagrant up.

```
vagrant reload
```

5. **vagrant suspend**: Suspends the running Vagrant environment, saving its current state.
```
vagrant suspend
```

6. **vagrant resume**: Resumes a previously suspended Vagrant environment.
```
vagrant resume
```

7. **vagrant destroy**: Stops and deletes the Vagrant environment, including all associated virtual machines and resources.

```
vagrant destroy
```

8. **vagrant status**: Shows the current status of the Vagrant environment.
```
vagrant status
```

9. **vagrant ssh**: Connects to the Vagrant environment using SSH.
```
vagrant ssh
```

10. **vagrant provision**: Runs the provisioners defined in the Vagrantfile on the running Vagrant environment.

```
vagrant provision
```

11. **vagrant box list**: Lists all the boxes installed on your local machine.

```
vagrant box list
```

12. **vagrant box add**: Adds a new box to your local machine, either from a URL or a local file.

```
vagrant box add [box_name] [box_url_or_path]
```

13. **vagrant box update**: Updates an installed box to the latest version.

```
vagrant box update --box [box_name]
```

13. **vagrant box remove**: Removes a box from your local machine.
```
vagrant box remove [box_name]
```

### Vagrant Best Practices

While working with Vagrant boxes in our tech stack, please keep the following best practices in mind:

1. **Use shared folders**: Configure shared folders between your host machine and the VM to easily transfer files and
   maintain a single source of truth for your project files. In this project, the important OreSat GitHub repositories are
   cloned and shared with the VM.

2. **Backup your work**: Although Vagrant boxes provide a consistent environment, it's still essential to regularly
   backup your work. Commit your changes to the Git repository and push them to the remote server.

3. **Stay in sync with your team**: Keep the Vagrantfile and any provisioning scripts up to date with the latest changes
   from your team. This ensures that your Vagrant box stays consistent with the project requirements.