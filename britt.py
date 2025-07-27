from seleniumbase import SB


with SB(uc=True, test=True) as britt:

    if True:
        url = "https://kick.com/brutalles"
        britt.uc_open_with_reconnect(url, 5)
        britt.uc_gui_click_captcha()
        britt.sleep(1)
        britt.uc_gui_handle_captcha()
        britt.sleep(1)
        if britt.is_element_present('button:contains("Accept")'):
            britt.uc_click('button:contains("Accept")', reconnect_time=4)
        if britt.is_element_visible('#injected-channel-player'):
            while britt.is_element_visible('#injected-channel-player'):
                britt.sleep(10)
