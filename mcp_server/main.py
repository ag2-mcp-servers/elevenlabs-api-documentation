# generated by fastapi-codegen:
#   filename:  openapi.yaml
#   timestamp: 2025-06-28T18:56:14+00:00



import argparse
import json
import os
from typing import *
from typing import Any, Optional, Union

from autogen.mcp.mcp_proxy import MCPProxy
from autogen.mcp.mcp_proxy.security import BaseSecurity
from fastapi import Header, UploadFile

from models import (
    AddVoiceResponseModel,
    BodyDeleteHistoryItemsV1HistoryDeletePost,
    BodyDownloadHistoryItemsV1HistoryDownloadPost,
    BodyTextToSpeechV1TextToSpeechVoiceIdPost,
    BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost,
    ExtendedSubscriptionResponseModel,
    GetHistoryResponseModel,
    GetVoicesResponseModel,
    HTTPValidationError,
    UserResponseModel,
    V1VoicesVoiceIdSettingsEditPostRequest,
    VoiceResponseModel,
    VoiceSettingsResponseModel,
)

app = MCPProxy(
    description="This is the documentation for the ElevenLabs API. You can use this API to use our service programmatically, this is done by using your xi-api-key. <br/> You can view your xi-api-key using the 'Profile' tab on https://beta.elevenlabs.io. Our API is experimental so all endpoints are subject to change.",
    title='ElevenLabs API Documentation',
    version='1.0',
    servers=[{'url': 'https://api.elevenlabs.io/'}],
)


@app.get(
    '/v1/history',
    description=""" Returns metadata about all your generated audio. """,
    tags=['history_item_management'],
)
def get_generated_items_v1_history_get(
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Get Generated Items
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/history/delete',
    description=""" Delete a number of history items by their IDs. """,
    tags=['history_item_management'],
)
def delete_history_items_v1_history_delete_post(
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
    body: BodyDeleteHistoryItemsV1HistoryDeletePost = ...,
):
    """
    Delete History Items
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/history/download',
    description=""" Download one or more history items. If one history item ID is provided, we will return a single audio file. If more than one history item IDs are provided, we will provide the history items packed into a .zip file. """,
    tags=['history_item_management'],
)
def download_history_items_v1_history_download_post(
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
    body: BodyDownloadHistoryItemsV1HistoryDownloadPost = ...,
):
    """
    Download History Items
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/history/{history_item_id}',
    description=""" Delete a history item by its ID """,
    tags=['history_item_management'],
)
def delete_history_item_v1_history__history_item_id__delete(
    history_item_id: str, xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Delete History Item
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/history/{history_item_id}/audio',
    description=""" Returns the audio of an history item. """,
    tags=['history_item_management', 'audio_sample_handling'],
)
def get_audio_from_history_item(
    history_item_id: str, xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Get Audio From History Item
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/text-to-speech/{voice_id}',
    description=""" Converts text into speech using a voice of your choice and returns audio. """,
    tags=['text_to_speech_conversion', 'voice_settings_management'],
)
def text_to_speech_v1_text_to_speech__voice_id__post(
    voice_id: str,
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
    body: BodyTextToSpeechV1TextToSpeechVoiceIdPost = ...,
):
    """
    Text To Speech
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/text-to-speech/{voice_id}/stream',
    description=""" Converts text into speech using a voice of your choice and returns audio as an audio stream. """,
    tags=['text_to_speech_conversion', 'voice_settings_management'],
)
def text_to_speech_v1_text_to_speech__voice_id__stream_post(
    voice_id: str,
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
    body: BodyTextToSpeechV1TextToSpeechVoiceIdStreamPost = ...,
):
    """
    Text To Speech
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/user',
    description=""" Gets information about the user """,
    tags=['user_profile_management'],
)
def get_user_info_v1_user_get(
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Get User Info
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/user/subscription',
    description=""" Gets extended information about the users subscription """,
    tags=['user_profile_management'],
)
def get_user_subscription_info_v1_user_subscription_get(
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Get User Subscription Info
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/voices',
    description=""" Gets a list of all available voices for a user. """,
    tags=['voice_settings_management', 'text_to_speech_conversion'],
)
def get_voices_v1_voices_get(
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Get Voices
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/voices/add',
    description=""" Add a new voice to your collection of voices in VoiceLab. """,
    tags=['text_to_speech_conversion', 'voice_settings_management'],
)
def add_voice_v1_voices_add_post(
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'), file: UploadFile = ...
):
    """
    Add Voice
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/voices/settings/default',
    description=""" Gets the default settings for voices. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app. """,
    tags=['voice_settings_management', 'text_to_speech_conversion'],
)
def get_default_voice_settings__v1_voices_settings_default_get():
    """
    Get Default Voice Settings.
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/voices/{voice_id}',
    description=""" Deletes a voice by its ID. """,
    tags=['voice_settings_management'],
)
def delete_voice_v1_voices__voice_id__delete(
    voice_id: str, xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Delete Voice
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/voices/{voice_id}',
    description=""" Returns metadata about a specific voice. """,
    tags=['text_to_speech_conversion', 'voice_settings_management'],
)
def get_voice_v1_voices__voice_id__get(
    voice_id: str,
    with_settings: Optional[bool] = False,
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
):
    """
    Get Voice
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/voices/{voice_id}/edit',
    description=""" Edit a voice created by you. """,
    tags=['voice_settings_management', 'audio_sample_handling'],
)
def edit_voice_v1_voices__voice_id__edit_post(
    voice_id: str,
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
    file: UploadFile = ...,
):
    """
    Edit Voice
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.delete(
    '/v1/voices/{voice_id}/samples/{sample_id}',
    description=""" Removes a sample by its ID. """,
    tags=['audio_sample_handling'],
)
def delete_sample_v1_voices__voice_id__samples__sample_id__delete(
    voice_id: str,
    sample_id: str = ...,
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
):
    """
    Delete Sample
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/voices/{voice_id}/samples/{sample_id}/audio',
    description=""" Returns the audio corresponding to a sample attached to a voice. """,
    tags=['audio_sample_handling'],
)
def get_audio_from_sample(
    voice_id: str,
    sample_id: str = ...,
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
):
    """
    Get Audio From Sample
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.get(
    '/v1/voices/{voice_id}/settings',
    description=""" Returns the settings for a specific voice. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app. """,
    tags=['text_to_speech_conversion', 'voice_settings_management'],
)
def get_voice_settings_v1_voices__voice_id__settings_get(
    voice_id: str, xi_api_key: Optional[str] = Header(None, alias='xi-api-key')
):
    """
    Get Voice Settings
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


@app.post(
    '/v1/voices/{voice_id}/settings/edit',
    description=""" Edit your settings for a specific voice. "similarity_boost" corresponds to"Clarity + Similarity Enhancement" in the web app and "stability" corresponds to "Stability" slider in the web app. """,
    tags=['text_to_speech_conversion', 'voice_settings_management'],
)
def edit_voice_settings_v1_voices__voice_id__settings_edit_post(
    voice_id: str,
    xi_api_key: Optional[str] = Header(None, alias='xi-api-key'),
    body: V1VoicesVoiceIdSettingsEditPostRequest = ...,
):
    """
    Edit Voice Settings
    """
    raise RuntimeError("Should be patched by MCPProxy and never executed")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="MCP Server")
    parser.add_argument(
        "transport",
        choices=["stdio", "sse", "streamable-http"],
        help="Transport mode (stdio, sse or streamable-http)",
    )
    args = parser.parse_args()

    if "CONFIG_PATH" in os.environ:
        config_path = os.environ["CONFIG_PATH"]
        app.load_configuration(config_path)

    if "CONFIG" in os.environ:
        config = os.environ["CONFIG"]
        app.load_configuration_from_string(config)

    if "SECURITY" in os.environ:
        security_params = BaseSecurity.parse_security_parameters_from_env(
            os.environ,
        )

        app.set_security_params(security_params)

    mcp_settings = json.loads(os.environ.get("MCP_SETTINGS", "{}"))

    app.get_mcp(**mcp_settings).run(transport=args.transport)
