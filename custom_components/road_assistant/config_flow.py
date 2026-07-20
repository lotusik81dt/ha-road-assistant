import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from .const import DOMAIN, CONF_COUNTRY, CONF_LANGUAGE, DEFAULT_COUNTRY, DEFAULT_LANGUAGE

class RoadAssistantConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Obsługa konfiguracji GUI dla Road Assistant."""

    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="HA Road Assistant", data=user_input)

        data_schema = vol.Schema(
            {
                vol.Required(CONF_COUNTRY, default=DEFAULT_COUNTRY): str,
                vol.Required(CONF_LANGUAGE, default=DEFAULT_LANGUAGE): str,
            }
        )

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
