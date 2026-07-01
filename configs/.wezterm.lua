-- Pull in the wezterm API
local wezterm = require 'wezterm'

-- This will hold the configuration.
local config = wezterm.config_builder()

-- This is where you actually apply your config choices.

-- UI configs
config.color_scheme = 'AdventureTime'
-- config.color_scheme = 'Ayu Mirage'
config.window_background_opacity = 0.9
config.macos_window_background_blur = 50
config.font_size = 14.0
config.max_fps = 120
config.enable_tab_bar = true
config.hide_tab_bar_if_only_one_tab = true
config.window_decorations = "RESIZE"
config.inactive_pane_hsb = {
	saturation = 0.9,
	brightness = 0.7,
}
-- For example, changing the initial geometry for new windows:
config.initial_cols = 120
config.initial_rows = 28

-- Finally, return the configuration to wezterm:
return config


