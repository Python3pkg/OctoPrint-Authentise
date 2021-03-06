# coding=utf-8


import octoprint.plugin


class SettingsPlugin(octoprint.plugin.SettingsPlugin):
    def get_settings_defaults(self):
        return dict(
            api_key=None,
            api_secret=None,
            authentise_url='https://print.authentise.com',
            authentise_user_url='https://users.authentise.com',
            streamus_client_path='authentise',
            streamus_config_path=None,
            frame_src='https://app.authentise.com/#/models',
        )
