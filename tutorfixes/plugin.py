from tutor import hooks

hooks.Filters.ENV_PATCHES.add_item(
    ("mfe-dockerfile-pre-npm-install", "RUN npm -g i npm@8.19.4")
)
