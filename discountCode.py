import requests
from bs4 import BeautifulSoup
import pandas as pd

"""
waitrose ---
<div class="promotion-discount-card promotion-discount-card--condensed editable border w-100" data-promotion-group="sales" data-promotion-card="" data-promotion-modal-link="https://www.nme.com/discount-codes/discount-codes/visit/promotion/69524" data-promotion-id="69524" data-promotion-title="Waitrose Rewards: Enjoy exclusive offers and discounts up to 20% off select items" data-promotion-query="c"><div class="promotion-discount-card__main d-none d-md-flex"><div class="promotion-discount-card__discount  p-3" style="color: #ffffff; background-color: #568721;"><h4 class="discount"><div class="discount__amount">20%</div><div class="discount__text">OFF</div><div class="discount__type mt-5">SALE</div></h4></div><div class="d-flex justify-content-between truncate-fix w-100"><div class="promotion-discount-card__info d-flex flex-column justify-content-between align-items-center align-items-md-start"><h3 class="promotion-discount-card__info__title title-sm font-weight-bold">Waitrose Rewards: Enjoy exclusive offers and discounts up to 20% off select items</h3><div class="promotion-discount-card__info__description font-secondary text-lg mt-3">
                    Join myWaitrose membership and start saving on select items, get member-only discounts, and more perks as a member.
                </div><div class="mt-4 d-flex"><div class="promotion-usage d-flex text-sm "><div class="font-weight-bold">
        61 people used today
    </div></div></div></div><div class="promotion-discount-card__btn"><div class="btn btn-primary text-uppercase">
                            GET DEAL
                        </div></div></div></div><div class="promotion-discount-card__mobile d-md-none p-3 "><div class="promotion-discount-card__mobile-body d-flex align-items-center justify-content-between mb-3"><div class=""><div class="d-flex mb-3"><h3 class="promotion-discount-card__mobile-body__title font-weight-bold m-0">
                    Waitrose Rewards: Enjoy exclusive offers and discounts up to 20% off select items
                </h3></div><div class="" data-shave="" data-shave-height="40" style="">
                Join myWaitrose membership and start saving on select items, get member-only discounts, and more perks as a member.
            </div></div><div class="font-weight-bold pl-3"><div class="promotion-discount-card__mobile-body__button"><svg class="svg-inline--fa fa-chevron-circle-right fa-w-16" aria-hidden="true" focusable="false" data-prefix="fal" data-icon="chevron-circle-right" role="img" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 512 512" data-fa-i2svg=""><path fill="currentColor" d="M8 256c0 137 111 248 248 248s248-111 248-248S393 8 256 8 8 119 8 256zM256 40c118.7 0 216 96.1 216 216 0 118.7-96.1 216-216 216-118.7 0-216-96.1-216-216 0-118.7 96.1-216 216-216zm86.6 224.5l-115.1 115c-4.7 4.7-12.3 4.7-17 0l-7.1-7.1c-4.7-4.7-4.7-12.3 0-17L303 256l-99.5-99.5c-4.7-4.7-4.7-12.3 0-17l7.1-7.1c4.7-4.7 12.3-4.7 17 0l115.1 115c4.6 4.8 4.6 12.4-.1 17.1z"></path></svg><!-- <i class="fal fa-chevron-circle-right"></i> --></div></div></div><div class="d-flex justify-content-between align-items-center"><div class="promotion-discount-card__mobile-body__discount text-uppercase font-weight-bold">
            20% Off
        </div><div class="promotion-discount-card__mobile-body__usage"><div class="promotion-usage d-flex text-sm "><div class="font-weight-bold">
        61 people used today
    </div></div></div></div></div></div>
    
    
grabfood ---
<div class="item procoupon_item--voucher" data-coupon-type="code" data-logo-url="https://www.sgdtips.com/wp-content/uploads/GrabFood-logo.png" data-onclick="" data-goto-url="https://clk.omgt3.com/c/?AID=1051559&amp;PID=38846">
<div class="sgdtpro_voucher-content">
<div class="pro-col col-discount">
<div class="voucher-dis">
<p><span class="percent-disc">S$10</span></p>
<p class="status-act"><span>OFF</span></p>
<p class="voucher-captions"><span class="pro-code">CODE</span></p>
</div>
</div>
<div class="pro-col col-detail">
<h3 class="sgdt-brief-promo promo-code-h3">GrabFood promotion code for Citi cardmembers: S$10 off</h3>
<input class="sgdt_code-value" type="hidden" value="CITI10"> <div class="show-detail">
<span class="sgdtprom-show--detail">See detail <i class="fa fa-angle-down"></i></span>
<p class="sts-verified"><span></span></p>
</div>
</div>
<a href="#coupon-0" target="_blank" class="sgdtpro-btn--offer sgdton-click-item btn-offer" data-onclick="" data-goto-url="https://clk.omgt3.com/c/?AID=1051559&amp;PID=38846">
<span class="see-the-offer"><span>SEE CODE</span><span class="corner"></span></span>
</a>
<a href="#coupon-0" target="_blank" class="sgdton-click-item-wrapper" data-onclick="" data-goto-url="https://clk.omgt3.com/c/?AID=1051559&amp;PID=38846"><span class="btn-arr hidden-desktop sgdton-click-item"><i class="fa fa-angle-right"></i></span></a>
</div>
<div class="sgdtpro_content-detail">
<div class="sgdtcontent-detail"><p class="sgdtcontent-text">Spend at least S$50 on your GrabFood order and enjoy <strong>S$10 off</strong> using this above coupon code. Promo code is valid till 31 Mar 2023.</p></div>
</div>
</div>
"""
def promo_code_scraper(soup):
    """
    The web scraper code is very specific for each individual website, so likely it won't work if you change the
    website link to another one, or the website changes its format subsequently.
    :param soup: the output from beautifulsoup module
    :return: the voucher_df in pandas df format.
    """
    voucher_desc_lst = []
    voucher_code_lst = []
    voucher_detail_lst = []
    for item in soup.select(".promotion-discount-card.promotion-discount-card--condensed.editable.border.w-100"):
        for voucher in item.select(".promotion-discount-card__main.d-none.d-md-flex"):
            for voucher_desc in voucher.select('.promotion-discount-card__info__title.title-sm.font-weight-bold'):
                voucher_desc_lst.append(voucher_desc.text)
            if not voucher.select('.sgdt_code-value'):
                voucher_code_lst.append('NA')
                voucher_detail_lst.append('NA')
            else:
                for code in voucher.select('.sgdt_code-value'):
                    # Here the get method helps to obtain the value filed in the hidden tag (.text is not working..)
                    voucher_code_lst.append(code.get('value'))
        for details in item.select(".sgdtpro_content-detail"):
            if not details.text.replace('\n', ''):
                voucher_detail_lst.append('NA')
            else:
                voucher_detail_lst.append(details.text.replace('\n', ''))


    for item in soup.select(".item.procoupon_item--voucher"):
        for voucher in item.select(".sgdtpro_voucher-content"):
            for voucher_desc in voucher.select('.sgdt-brief-promo.promo-code-h3'):
                voucher_desc_lst.append(voucher_desc.text)
            if not voucher.select('.sgdt_code-value'):
                voucher_code_lst.append('NA')
                voucher_detail_lst.append('NA')
            else:
                for code in voucher.select('.sgdt_code-value'):
                    # Here the get method helps to obtain the value filed in the hidden tag (.text is not working..)
                    voucher_code_lst.append(code.get('value'))
        for details in item.select(".sgdtpro_content-detail"):
            if not details.text.replace('\n', ''):
                voucher_detail_lst.append('NA')
            else:
                voucher_detail_lst.append(details.text.replace('\n', ''))

    voucher_df = pd.DataFrame(list(zip(voucher_desc_lst, voucher_code_lst, voucher_detail_lst)),
                              columns=['Description', 'Code', 'Details'])
    return voucher_df


websites = ["https://www.sgdtips.com/grabfood-promo-codes", "https://www.nme.com/discount-codes/waitrose.com"]
for website in websites:
    res = requests.get(website)
    soup = BeautifulSoup(res.text, "lxml")
    code = promo_code_scraper(soup)
    print(code)
    print("_____________________________________________")
