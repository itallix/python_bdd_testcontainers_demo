from testcontainers.general import DockerContainer
from os import environ


class DatastoreContainer(DockerContainer):
    """
    Datastore container for testing managed NoSQL Datastore.
    Example
    -------
    The example will spin up a Google Cloud Datastore emulator that you can use for integration tests.
    The :code:`ds` instance provides convenience method :code:`get_client` to connect to the emulator
    without having to set the emulator specific environment variables
    ::
        def test_docker_run_datastore():
            config = DatastoreContainer('google/cloud-sdk:latest')
            with config as ds:
                client = ds.get_client()
                query = client.query(kind="YOUR_ENTITY")
                ents = list(query.fetch())
    """

    def __init__(
        self,
        image="google/cloud-sdk:latest",
        project="test-project",
        port=8081,
        **kwargs,
    ):
        super(DatastoreContainer, self).__init__(image=image, **kwargs)
        self.project = project
        self.port = port
        self.with_exposed_ports(self.port)
        self.with_command(
            f"gcloud beta emulators datastore start --project={self.project} "
            f"--host-port=0.0.0.0:{self.port} "
            "--verbosity=error --consistency=1.0 --no-store-on-disk"
        )

    def get_client(self):
        from google.cloud import datastore

        emulator_host = (
            f"{self.get_container_host_ip()}:{self.get_exposed_port(self.port)}"
        )
        environ["DATASTORE_DATASET"] = self.project
        environ["DATASTORE_EMULATOR_HOST"] = emulator_host
        environ["DATASTORE_EMULATOR_HOST_PATH"] = f"{emulator_host}/datastore"
        environ["DATASTORE_HOST"] = f"http://{emulator_host}"
        environ["DATASTORE_PROJECT_ID"] = self.project
        return datastore.Client()
