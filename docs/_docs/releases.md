---
title: Release Management
permalink: /docs/releases/
---

## Release Management

CSLE has semantic versioning, i.e., versions of CSLE are of the form `MAJOR.MINOR.PATCH`.

- The `MAJOR` version is incremented when incompatible API changes are made.
- The `MINOR` version is incremented new functionality is added in a backwards compatible manner.
- The `PATCH` version is incremented when backwards compatible bug fixes are made.

To generate a new release of CSLE, the following steps must be performed:

1. Publish new versions of the Python libraries to: <a href="https://pypi.org/">https://pypi.org/</a>.
2. Publish new versions of the Docker containers to: <a href="https://hub.docker.com/">https://hub.docker.com/</a>.
3. Publish a new version of the documentation to: <a href="http://limmen.dev/csle">http://limmen.dev/csle</a>.
4. Make a GitHub release with all artifacts (<a href="https://github.com/Limmen/csle">https://github.com/Limmen/csle</a>).

**Python releases.** To make a new Python release, do the following:

1. Copy the `csle/simulation_system/libs/.pypirc_template` file to your home directory and rename it to `.pypirc`, e.g., `/home/kim/.pypirc`.
2. Create a PyPi token following the intructions <a href="https://pypi.org/manage/account/token/">here</a>.
3. Add the PyPi token to the `.pypirc` file.
4. Edit the `RELEASE_CONFIG` variable to match the versions of the release in the file:
    ```bash
     ./simulation-system/libs/make_release.py
    ```
   <p class="captionFig">
   Listing 143: File to generate Python releases.
   </p>

5. Run the command below to build all the Python libraries and push the built artifacts to PyPi:
    ```bash
     python ./simulation-system/libs/make_release.py
    ```
   <p class="captionFig">
   Listing 144: Command to generate a new Python release.
   </p>

**Documentation releases.** After making a new Python release, 
the new API documentation can be generated by running the command:

```bash
simulation-system/libs/generate_docs.sh
```

<p class="captionFig">
Listing 145: Command to generate release documentation.
</p>

**Docker releases.** To make a new Docker release, do the following:

1. Edit the `VERSION` variable in the file:
    ```bash
    ./emulation-system/base_images/Makefile
    ```
   <p class="captionFig">
   Listing 146: Makefile for base Docker images in CSLE.
   </p>
2. Edit the `VERSION` variable in the file:
     ```bash 
      ./emulation-system/derived_images/Makefile
     ```
   <p class="captionFig">
   Listing 147: Makefile for derived Docker images in CSLE.
   </p>
3. Edit the versions of the derived images in the Dockerfiles inside the following directory:
    ```bash
     ./emulation-system/derived_images/
    ```
   <p class="captionFig">
   Listing 148: Directory with derived Docker images in CSLE.
   </p>
4. Edit the versions of the base images in the Dockerfiles inside the following directory:
    ```bash
     ./emulation-system/base_images/
    ```
   <p class="captionFig">
   Listing 149: Directory with base Docker images in CSLE.
   </p>   
5. Edit the version parameters in all emulation configurations in the following directory:
   ```bash
   ./emulation-system/envs
   ```
   <p class="captionFig">
   Listing 150: Directory with emulation configurations.
   </p>
6. Make a new release of `https://github.com/Limmen/exploit-CVE-2017-7494`:
    - Clone the repo by runnign the command: `git clone https://github.com/Limmen/exploit-CVE-2017-7494`
    - Update the version parameter in `exploit-CVE-2017-7494/Makefile`
    - Build: `cd exploit-CVE-2017-7494; make build`
    - Push: `cd exploit-CVE-2017-7494; make push`
6. Build the images by running the command:
    ```bash
      cd emulation-system/; make build
    ```
   <p class="captionFig">
   Listing 151: Command to build the Docker images in CSLE.
   </p>
7. Push the images to DockerHub by running the command:
    ```bash
     cd emulation-system/; make push
    ```
   <p class="captionFig">
   Listing 152: Command to push Docker images to DockerHub.
   </p>
8. Insert the new emulation configuration into the metastore by running the command:
    ```bash
     cd emulation-system/; make emulations
    ```
   <p class="captionFig">
   Listing 153: Command to insert emulation configurations into the metastore.
   </p>

**GitHub releases.** To make a release in GitHub, 
follow the <a href="https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository">official guide</a>.

