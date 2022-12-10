import time
from bot.bot import Bot
from revChatGPT.revChatGPT import Chatbot

config = {
    "Authorization": "<Your Bearer Token Here>",  # This is optional
    "session_token": "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0.._BniuRSwMqdGn8t2.Hv_C4nsWF1FWnVGxNs19YZOGLDIWFlyC3FeLlTE9HUEgV1M8IFmhz1aH0j40vutVTzoEv3JDSEZN8je4kzewXE5tcKqhQF_Jh0SSHNL52OdRe_tqu_aE61L39NkvxEkmMRP2teXmWtiBIGtrPX3B77IbHIyqx9Kbk17awwl_WJokr39KlWhHE-Mpf9AwPvOW4UPi2csIxVNsVFW6MjxffRL8QZAqhXaeVlAnpjlpfJrK1B9TRoH7wkj0Q4nQ4MMhenvKXQHhOaa2tfTC79BeOBr8d60b2HPGCiOZuYc4vCqehXRl4VA7_JF9EKEmhgBQAPp0J1LFTC-3i0ZVAUX4zud8UEAsAwkjknQx7BHx9_QUOGil5I4U84WWzsGKxNNj1Jhi3z877V6d90CrTQax_yuuNzV9wb7j_RYx5EbO1MKmOPvL1iksa7xm0SYWsK2fYUID2vW2cE0nAavnGyi7g2-Lf83ARyWAmU8puuEweuEbsS_-1-IP6b3rtapOoZWfWmW74Mm6mmdxBIldrKHTDK8rJanjbp5Dho4YdJaTlAo7Mlg6fwpFk5i-2_QPr-s2E141hLCAhbKFQ6OTKfv3yugF1OoOG0IsXy49yuq3ezznDhtArYgZ6mj-DfHaQakuYrw9aHsfHebiVZ6tuwr_lZr73AuwneD0wGc1sk5nTYqFGn-E9ZC3kgng5Sa_CrOg2RhuNPsuDDsDuJ22ANilQprmDR0N8J-2ASlqkyf_af23QWwaEmjj8pcDrg_FWs7-6Qdju4pSFcLbtbAFh9ORi5SD463LxGxHsRPNCL9LfUZFrVFYVfTKk3mGtb7XQ80p7L1O7_ix6UkiastENknqH-cwk6HCW8VKf2ASp28NoEhKCjW0CHfGT4eHQxxzh2wrb2FWmw7zAXd8_c48o1LY6GOgqBWnp4npMYRwA2yki0cuKR5eVrKHlZZU4g5hSQ5F_Pq0qDZsCrKFCUJ19C3ndqG0XZF70jUfJtTMdUgFh4viDVpVS4FvL35VDTygYnTz7DCRHc9uLlsG8e-7wfCHRcyL8U4HL1KTB2JIZnNMOAHaeiTxAc9PeLxhqSHuG7LttdHPWE0OBUZmMbArR9BzjHp4L3mL-oK8xGil9vuw43TWxpPpcbP_EzuZIBgWlTB4LZg19WmrRq_Ll1eLjXKeCEzoxisyicIdQ8q01iPKZOfVQZCISmgG8Ey6qm8DAk84tJ44p7IWXeE5Ho-SIdW1aR9H7U02ycvtBM24aRs30o_xwqfKfDInrAUsGeJAkA4iKkmUtzaHHYlBZVAITG7-FlsFBgDJQStG7w_4d-JqfqltO6YrbZG2A5EYX8RV5SFgNzEluTp_ZY0A65kThVLvVnldWGb0gkBiC8r-UzYKGgQQJwG-WqnyOvQ5oNMqUErqWaqYg8Z1u7nvZlFG_WeqwfF711huA2eMLIyV3gvdhxSVO9j2IfNsxQoMOIeUcXF_d64q95RgM2Cv5bw-kwRSqumejPhGghjDwv01et6zeHnseoEItHkyfKHw443rqBvitMlERQcvIfF07j0Pgm2-7fBiGFAstS-6swFnydmlKev9ypAKE-vFgH_R4s5R0cy_aYQr16rpmX0pRaDfEA-kDrq4u1PFUijuRQiOG0UN3Ih4E7HPZtKvCqQreUbceihgWsh0_u-Ygh6dpN7-ALf4En6e--FyRePScJ1RUHByJZ_r5R9tPgdFDmC2N38ybXA9CUjHh7uVZtlC5Gb78He5kRqTCKGV-lVqBzubaI-VO-oQfEyui81I3e1XpAAQySITT6d1HtM9HyEk0_CMQ83N5mpUAKaCWT-Pqzby-GmKfet-ct07NiH-8yvvgThMEAl78bk-W8MBjQB6fagHjR93OWMr6usow4noL5sf1gVa1izd1_OLbroUY8kFHN7BCryHsy-WmFnfUzNb6qS-7HsX4qsoBAHmQMlYRj-B9RMa7QC_53f8laQPMnT4c1M1d1yITarmtL9n6cL0Ku096w3c-4735yk-mYpds0KaAclU9_7NjcznEcY3NHRr0LxwxoV6-ClHFO6Ccqgxyk-Kng0J3oGYwgY4QBPuSCphvf9PmbhABeLILx0i-_eeI3gOfAKbZUGDweftoG1Lw7qgB14KOX1fig69PFxp8dGApMOTJvQeXWN7ISPlDZRfmRkSbO5siDsTS4WS01qcgdc_2osmN8aMyB_bP-FG4v3CF8z6Cpp6x-iIyXdHS_riNGydbf5-Et1e5nlYTRAVW4Cgf-P_AAZH82PGIpWsPWO3Lsisli1IdVSHi5Vxfj8OzzE0aC5CuXzvCv18KwCyDgHZ2AZeqGkBHPyptmXyIPspaSlRtq7H7j5w57deaOmJVjHM.iOPoBiz9LmbJxxXkoKyzfQ"
}
chatbot = Chatbot(config)
user_session = dict()
last_session_refresh = time.time()


class ChatGPTBot(Bot):
    def reply(self, query, context=None):
        from_user_id = context['from_user_id']
        if from_user_id in user_session:
            if time.time() - user_session[from_user_id]['last_reply_time'] < 60 * 3:
                chatbot.conversation_id = user_session[from_user_id]['conversation_id']
                chatbot.parent_id = user_session[from_user_id]['parent_id']
        else:
            chatbot.reset_chat()

        now = time.time()
        global last_session_refresh
        if now - last_session_refresh > 60 * 10:
            chatbot.refresh_session()
        last_session_refresh = now

        res = chatbot.get_chat_response(query, output="text")

        user_cache = dict()
        user_cache['last_reply_time'] = time.time()
        user_cache['conversation_id'] = res['conversation_id']
        user_cache['parent_id'] = res['parent_id']
        user_session[from_user_id] = user_cache

        print("[GPT]user={}, convId={}, content={}", from_user_id, res['conversation_id'], res['message'])
        return res['message']

