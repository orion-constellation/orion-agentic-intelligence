import pytest
import asyncio 
import aiohttp


# Successful GET request returns expected data
    
@pytest.mark.asyncio
async def test_successful_get_request_returns_expected_data(self, mocker):
    mocker.patch('orion_agentsV2.api.AsyncAPIClient.get', return_value={"key": "value"})
    client = mocker.Mock()
    client.get.return_value = asyncio.Future()
    client.get.return_value.set_result({"key": "value"})

    await main()

    client.get.assert_called_once_with("resource")
    assert client.get.return_value.result() == {"key": "value"}
    

@pytest.mark.asyncio
async def test_get_request_to_non_existent_endpoint_handles_404_error_gracefully(self, mocker):
    mocker.patch('orion_agentsV2.api.AsyncAPIClient.get', side_effect=aiohttp.ClientResponseError(
        request_info=mocker.Mock(), history=(), status=404, message="Not Found"
    ))
    client = mocker.Mock()
    client.get.side_effect = aiohttp.ClientResponseError(
        request_info=mocker.Mock(), history=(), status=404, message="Not Found"
    )

    with pytest.raises(aiohttp.ClientResponseError) as excinfo:
        await main()

    assert excinfo.value.status == 404
    assert excinfo.value.message == "Not Found"