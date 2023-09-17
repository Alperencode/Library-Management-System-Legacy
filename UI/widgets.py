from CTkMessagebox import CTkMessagebox


def WarningMessage(text):
    CTkMessagebox(
        title="Warning",
        message=text,
        icon="warning", option_1="Retry"
        )
