# coding=utf-8


import octoprint.plugin


class AssetPlugin(octoprint.plugin.AssetPlugin):
    def get_assets(self):
        return dict(
            js=[
                "js/connect.js",
                "js/models.js",
            ],
            less=["less/authentise.less"],
        )
