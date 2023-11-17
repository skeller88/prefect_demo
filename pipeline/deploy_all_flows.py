if __name__ == "__main__":
    worker_pool = "worker_pool"
    # gets all currently deployed flows
    import asyncio
    from prefect.client import get_client


    async def get_flows():
        client = get_client()
        r = await client.read_flows(limit=5)
        return r


    r = asyncio.run(get_flows())

    # get all the local flows
    for flow in flows:
        # flow has changed, replace deployed flow with new flow
        flow.deploy(
            name=flow.name,
            work_pool_name=worker_pool,
            image="discdiver/no-build-image:1.0",
            build=False
        )

        # if deployed flow no longer exists locally, delete