# -*- coding: utf-8 -*-
# (c) YashDK [yash-dk@github]

from telethon.tl.functions.channels import GetParticipantRequest
from telethon.tl.types import ChannelParticipantAdmin,ChannelParticipantCreator,ChannelParticipantsAdmins
import logging,traceback
from ..core.getVars import get_val
torlog = logging.getLogger(__name__)

#todo add alpha admin if needed

async def is_admin(client,user_id,chat_id, force_owner=False):
            print(user_id)
            return True
