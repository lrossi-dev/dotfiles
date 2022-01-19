# -*- coding: utf-8 -*-
from libqtile.dgroups import simple_key_binder
import os
import re
import socket
import subprocess
import yaml
from libqtile import qtile
from libqtile.config import Click, Drag, Group, KeyChord, Key, Match, Screen
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
from typing import List  # noqa: F401from typing import List  # noqa: F401

mod = "mod4"              # Sets mod key to SUPER/WINDOWS
myTerm = "st"      # My terminal of choice
myBrowser = "brave"  # My browser of choice

colors = {'color0': '#282c34', 'color1': '#e06c75', 'color2': '#98c379', 'color3': '#e5c07b', 'color4': '#61afef', 'color5': '#c678dd', 'color6': '#56b6c2', 'color7': '#abb2bf',
          'color8': '#545862', 'color9': '#e06c75', 'color10': '#98c379', 'color11': '#e5c07b', 'color12': '#61afef', 'color13': '#c678dd', 'color14': '#56b6c2', 'color15': '#c8ccd4'}
font = 'Cantarell'
monofont = 'Inconsolata'

keys = [
    # The essentials
    Key([mod], "Return",
        lazy.spawn(myTerm),
        desc='Launches My Terminal'),
    Key([mod], "d",
        lazy.spawn("dmenu_run -fn '{font}:pixelsize=13' -nb '{nb}' -nf '{nf}' -sb '{sb}' -sf '{sf}' -l 20 -p 'Run: '".format(
            font=font, nb=colors['color0'], nf=colors['color7'], sb=colors['color4'], sf=colors['color0'])),
        desc='Run Launcher'),
    Key([mod], "f",
        lazy.spawn(myBrowser),
        desc='Browser'),
    Key([mod], "Tab",
        lazy.next_layout(),
        desc='Toggle through layouts'),
    Key([mod], "q",
        lazy.window.kill(),
        desc='Kill active window'),
    Key([mod, "shift"], "r",
        lazy.restart(),
        desc='Restart Qtile'),
    Key([mod, "shift"], "e",
        lazy.shutdown(),
        desc='Shutdown Qtile'),
    Key([mod], "x",
        lazy.spawn("slock"),
        desc='Screen locker'),
    Key([mod, "shift"], "x",
        lazy.spawn("shutdown -h now"),
        desc='System shutdown'),
    Key([mod, "control"], "r",
        lazy.spawn("reboot"),
        desc='System restart'),
    # System controls
    Key([mod], "F1",
        lazy.spawn('pamixer -t'),
        desc='Mute volume'),
    Key([mod], 'F2',
        lazy.spawn('pamixer --allow-boost -d 5'),
        desc='Decrease volume by 5%'),
    Key([mod], 'F3',
        lazy.spawn('pamixer --allow-boost -i 5'),
        desc='Increase volume by 5%'),
    # Treetab controls
    Key([mod, "shift"], "h",
        lazy.layout.move_left(),
        desc='Move up a section in treetab'),
    Key([mod, "shift"], "l",
        lazy.layout.move_right(),
        desc='Move down a section in treetab'),
    # Window controls
    Key([mod], "j",
        lazy.layout.down(),
        desc='Move focus down in current stack pane'
        ),
    Key([mod], "k",
        lazy.layout.up(),
        desc='Move focus up in current stack pane'
        ),
    Key([mod, "shift"], "j",
        lazy.layout.shuffle_down(),
        lazy.layout.section_down(),
        desc='Move windows down in current stack'
        ),
    Key([mod, "shift"], "k",
        lazy.layout.shuffle_up(),
        lazy.layout.section_up(),
        desc='Move windows up in current stack'
        ),
    Key([mod], "h",
        lazy.layout.shrink(),
        lazy.layout.decrease_nmaster(),
        desc='Shrink window (MonadTall), decrease number in master pane (Tile)'
        ),
    Key([mod], "l",
        lazy.layout.grow(),
        lazy.layout.increase_nmaster(),
        desc='Expand window (MonadTall), increase number in master pane (Tile)'
        ),
    Key([mod], "n",
        lazy.layout.normalize(),
        desc='normalize window size ratios'
        ),
    Key([mod], "m",
        lazy.layout.maximize(),
        desc='toggle window between minimum and maximum sizes'
        ),
    Key([mod, "shift"], "space",
        lazy.window.toggle_floating(),
        desc='toggle floating'
        ),
    Key([mod, "shift"], "f",
        lazy.window.toggle_fullscreen(),
        desc='toggle fullscreen'
        ),
    # Stack controls
    Key([mod, "shift"], "Tab",
        lazy.layout.rotate(),
        lazy.layout.flip(),
        desc='Switch which side main pane occupies (XmonadTall)'
        ),
    Key([mod], "space",
        lazy.layout.next(),
        desc='Switch window focus to other pane(s) of stack'
        ),
    Key([mod, "shift"], "space",
        lazy.layout.toggle_split(),
        desc='Toggle between split and unsplit sides of stack'
        ),
    # Dmenu scripts
    Key([mod, "control"], "e",
        lazy.spawn('dmenuemoji'),
        desc='Emoji picker with dmenu')
]

groups = [Group("🏠", layout='monadtall'),
          Group("🌎", layout='max'),
          Group("🎮", layout='floating'),
          Group("🧲", layout='monadtall'),
          Group("▶️", layout='monadtall'),
          Group("🐧", layout='monadtall'),
          Group("🦘", layout='monadtall'),
          Group("🌲", layout='monadtall'),
          Group("⭐", layout='monadtall'),
          Group("👻", layout='floating')]

# Allow MODKEY+[0 through 9] to bind to groups, see https://docs.qtile.org/en/stable/manual/config/groups.html
# MOD4 + index Number : Switch to Group[index]
# MOD4 + shift + index Number : Send active window to another Group
dgroups_key_binder = simple_key_binder("mod4")

layout_theme = {"border_width": 2,
                "margin": 8,
                "border_focus": "e1acff",
                "border_normal": "1D2330"
                }

layouts = [
    #layout.Tile(shift_windows=True, **layout_theme),
    # layout.VerticalTile(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.Max(**layout_theme),
    layout.TreeTab(
        font="Cantarell",
        fontsize=10,
        sections=["FIRST", "SECOND", "THIRD", "FOURTH"],
        section_fontsize=10,
        border_width=2,
        bg_color=colors['color0'],
        active_bg=colors['color5'],
        active_fg=colors['color0'],
        inactive_bg=colors['color0'],
        inactive_fg=colors['color7'],
        padding_left=0,
        padding_x=0,
        padding_y=5,
        section_top=10,
        section_bottom=20,
        level_shift=8,
        vspace=3,
        panel_width=200
    ),
    layout.Floating(**layout_theme)
]

##### DEFAULT WIDGET SETTINGS #####
widget_defaults = dict(
    font="Inconsolata Bold",
    fontsize=15,
    padding=3,
    background=colors['color0']
)
extension_defaults = widget_defaults.copy()


def init_widgets_list():
    widgets_list = [
        widget.Sep(
            linewidth=0,
            padding=6,
            foreground=colors['color7'],
            background=colors['color0']
        ),
        widget.GroupBox(
            font="Cantarell Bold",
            fontsize=10,
            margin_y=3,
            margin_x=0,
            padding_y=5,
            padding_x=3,
            borderwidth=3,
            active=colors['color5'],
            inactive=colors['color7'],
            rounded=False,
            highlight_color=colors['color0'],
            highlight_method="line",
            this_current_screen_border=colors['color5'],
            this_screen_border=colors['color5'],
            foreground=colors['color7'],
            background=colors['color0']
        ),
        widget.Sep(
            linewidth=0,
            padding=30,
            foreground=colors['color7'],
        ),
        widget.WindowName(
            foreground=colors['color4'],
            font='Inconsolata Bold',
            fontsize='15',
            padding=2
        ),
        widget.Systray(
            padding=5,
            margin=5,
            fontsize=12
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.TextBox(
            text="🌡️",
            padding=2,
            fontsize=12
        ),
        widget.ThermalSensor(
            threshold=90,
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=5
        ),
        widget.TextBox(
            text="🧠",
            padding=0,
            fontsize=14
        ),
        widget.CPU(
            format='{freq_current}GHz {load_percent}%',
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.TextBox(
            text="💽",
            padding=0,
            fontsize=14
        ),
        widget.Memory(
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn(myTerm + ' -e htop')},
            format='{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}',
            measure_mem='M',
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.TextBox(
            text="🔉",
            padding=0
        ),
        widget.PulseVolume(
            padding=5,
            mouse_callbacks={
                'Button1': lambda: qtile.cmd_spawn('pavucontrol' )
            }
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.CurrentLayoutIcon(
            custom_icon_paths=[os.path.expanduser("~/.config/qtile/icons")],
            padding=0,
            scale=0.7
        ),
        widget.CurrentLayout(
            padding=5
        ),
        widget.Sep(
            linewidth=0,
            padding=6,
        ),
        widget.Clock(
            format="📅 %A, %B %d 🕒 %H:%M "
        ),
    ]
    return widgets_list


def init_widgets_screen():
    widgets_screen = init_widgets_list()
    return widgets_screen


def init_screens():
    return [Screen(top=bar.Bar(widgets=init_widgets_screen(), opacity=1.0, size=20))]


if __name__ in ["config", "__main__"]:
    screens = init_screens()
    widgets_list = init_widgets_list()
    widgets_screen = init_widgets_screen()


def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


def window_to_previous_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i != 0:
        group = qtile.screens[i - 1].group.name
        qtile.current_window.togroup(group)


def window_to_next_screen(qtile):
    i = qtile.screens.index(qtile.current_screen)
    if i + 1 != len(qtile.screens):
        group = qtile.screens[i + 1].group.name
        qtile.current_window.togroup(group)


def switch_screens(qtile):
    i = qtile.screens.index(qtile.current_screen)
    group = qtile.screens[i - 1].group
    qtile.current_screen.set_group(group)


def load_colors():
    with open("/home/lrossi/.cache/wal/colors.yaml", "r") as stream:
        try:
            return yaml.safe_load(stream)['colors']
        except Exception as exc:
            print(exc)
            return {'color0': '#282c34', 'color1': '#e06c75', 'color2': '#98c379', 'color3': '#e5c07b', 'color4': '#61afef', 'color5': '#c678dd', 'color6': '#56b6c2', 'color7': '#abb2bf', 'color8': '#545862', 'color9': '#e06c75', 'color10': '#98c379', 'color11': '#e5c07b', 'color12': '#61afef', 'color13': '#c678dd', 'color14': '#56b6c2', 'color15': '#c8ccd4'}


mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_app_rules = []  # type: List
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False

floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    # default_float_rules include: utility, notification, toolbar, splash, dialog,
    # file_progress, confirm, download and error.
    *layout.Floating.default_float_rules,
    Match(title='Confirmation'),      # tastyworks exit box
    Match(title='Qalculate!'),        # qalculate-gtk
    Match(wm_class='kdenlive'),       # kdenlive
    Match(wm_class='pinentry-gtk-2'),  # GPG key password entry
])
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True


@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.local/bin/autostart_blocking.sh'])


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
