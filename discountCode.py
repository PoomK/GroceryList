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


lidl ---



<article id="thread_483765" class="thread cept-thread-item cept-merchant-mode thread--type-list js-voucher-item cept-voucher-widget" data-track="{&quot;category&quot;:&quot;gutscheinsammler_widget&quot;}" data-t="partnerVoucher" data-t-d="{&quot;id&quot;:&quot;483765&quot;,&quot;name&quot;:&quot;voucherbox&quot;,&quot;merchantId&quot;:310}" data-t-view="" data-t-view-twig=""><div class="thread-bodySpace flex js-gutscheinsammler-item thread-clickRoot" data-handler="voucher-button" data-voucher-button="{&quot;id&quot;:&quot;gutscheinsammler_483765&quot;,&quot;url&quot;:null,&quot;isOffer&quot;:false,&quot;offerUrl&quot;:&quot;https://www.hotukdeals.com/visit/vbvoucher/2039/483765&quot;}" data-t="partnerVoucherLink" data-t-click="" tabindex="0" ,="" role="button"><div class="voucherBox-listDiscountCell--responsive bg--color-brandPrimaryPale text--color-charcoal voucherBox-listDiscountCell flex flex--dir-col flex--shrink-0 boxAlign-jc--all-c text--lh-1 bRad--a overflow--hidden box boxAlign-ai--all-c hide--toW3"><span class="flex boxAlign-center text--b cept-voucher-widget-item-discount-small size--all-l  size--fromW3-xxxl ">		
			£5
	</span><span class="size--all-xs size--fromW3-s cept-voucher-widget-item-discount-text text--lh-1-2 text--upper text--b hAlign--all-c space--h-1 overflow--wrap-break text--hyphens-a">Discount</span></div><div class="flex flex--dir-col flex--grow-1 width--max-12"><div class="flex--toW3 flex--dir-col"><div class="width--fromW3-7 box--all-i space--fromW3-l-3 space--mb-3 space--fromW3-mb-0"><div class="flex--toW3 boxAlign-ai--all-c boxAlign-ai--all-c"><div class="boxAlign-as--all-fs"><div class="voucherBox-listDiscountCell--responsive bg--color-brandPrimaryPale text--color-charcoal voucherBox-listDiscountCell flex flex--dir-col flex--shrink-0 boxAlign-jc--all-c text--lh-1 bRad--a overflow--hidden box boxAlign-ai--all-c hide--fromW3"><span class="flex boxAlign-center text--b cept-voucher-widget-item-discount-small size--all-l  size--fromW3-xl ">		
			£5
	</span><span class="size--all-xs size--fromW3-s cept-voucher-widget-item-discount-text text--lh-1-2 text--upper text--b hAlign--all-c space--h-1 overflow--wrap-break text--hyphens-a">Discount</span></div></div><div class="flex--grow-1 space--l-2 space--fromW3-l-0"><div class="thread-title--list--merchant-v2 size--fromW3-l space--fromW3-r-2 text--b cept-voucher-widget-item-title cept-thread-title--list--merchant js-thread-title">
		Take £5 off on Orders using Mobile App @ Lidl</div></div></div></div><div class="box--all-i vAlign--all-t width--fromW3-5"><span class="cept-voucher-widget-item-button voucher flex width--all-12 clickable"><span class="forceLayer zIndex--above lbox--v-4 overflow--hidden flex--grow-1 border border--color-brandPrimary bRad--a bRad--circle"><span class="lbox--v-4 boxAlign-ai--all-fs voucher-teaser width--all-12 hAlign--all-r bRad--toW3-t-r bRad--fromW3-l-r"><span class="lbox--v-4 boxAlign-jc--all-c size--all-m aGrid-item aGrid-item--r-0 space--r-2">OOD</span><span class="voucher-cover"></span><span class="voucher-flap"></span><span class="voucher-label aGrid-item lbox--v-4 boxAlign-jc--all-c size--all-m text--color-white text--b"><span class="hide--fromW2">Get code &amp; visit site*</span><span class="hide--toW2 hide--fromW3">Get code &amp; visit site*</span><span class="hide--toW3">Get code &amp; visit site*</span></span></span></span></span></div></div><div class="flex space--mt-a space--t-3 space--fromW3-l-3 space--fromW3-t-0"><div class="js-toggleDates flex boxAlign-ai--all-c flex--width-calc-fix space--mt-n1 text--color-greyShade"><div class="lbox--v-small space--mt-1 space--r-2 text--color-greyShade cept-expires-later"><svg width="17px" height="17px" class="icon icon--clock space--mr-1"><use xlink:href="/assets/img/ico_a8386.svg#clock"></use></svg><span class=" overflow--wrap-off size--all-s size--fromW3-m">Expires in 3 days</span></div><div class="lbox--v-small flex--width-calc-fix space--mt-1"><svg width="22px" height="14px" class="icon icon--trending space--mr-1"><use xlink:href="/assets/img/ico_a8386.svg#trending"></use></svg><span class="overflow--ellipsis size--all-s size--fromW3-m">Last used 4 m ago</span></div></div><span class="thread-noClick clickable space--ml-a text--b text--color-brandPrimary overflow--wrap-off size--all-s" data-handler="toggle" data-toggle="{&quot;events&quot;:[&quot;click&quot;],&quot;toggles&quot;:[{&quot;target&quot;:&quot;.js-voucher-item/.js-voucherDescription, .js-voucher-item/.js-toggleIcon&quot;,&quot;className&quot;:&quot;hide&quot;},{&quot;target&quot;:&quot;.js-voucher-item/.js-toggleDates&quot;,&quot;className&quot;:&quot;flex--wrap&quot;}],&quot;stopPropagation&quot;:true}"><span class="lbox--v-small boxAlign-ai--all-c js-toggleIcon">More info<svg width="10px" height="10px" class="icon icon--down js-toggleIcon space--ml-1 icon-d--1"><use xlink:href="/assets/img/ico_a8386.svg#down"></use></svg></span><span class="lbox--v-small boxAlign-ai--all-c js-toggleIcon hide">Less info<svg width="10px" height="10px" class="icon icon--up js-toggleIcon space--ml-1 hide icon-u--1"><use xlink:href="/assets/img/ico_a8386.svg#up"></use></svg></span></span></div></div></div><div class="js-voucherDescription thread-bodySpace width--all-12 space--t-0 hide"><p class="size--all-s text--lh-1-6"><strong class="text--b space--r-1">Minimum spend:</strong>£25</p><p class="size--all-s text--lh-1-6"><strong class="text--b space--r-1">Conditions:</strong>Some exclusions apply.</p></div></article>
"""


def promo_code_scraper():
    """
    The web scraper code is very specific for each individual website, so likely it won't work if you change the
    website link to another one, or the website changes its format subsequently.
    :param soup: the output from beautifulsoup module
    :return: the voucher_df in pandas df format.
    """

    websites = ["https://www.sgdtips.com/grabfood-promo-codes", "https://www.nme.com/discount-codes/waitrose.com"]

    voucher_desc_lst = []
    voucher_code_lst = []
    voucher_detail_lst = []
    link = []

    for website in websites:
        res = requests.get(website)
        soup = BeautifulSoup(res.text, "lxml")

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

        link = link + [website for i in range(len(voucher_desc_lst))]
        voucher_df = pd.DataFrame(list(zip(voucher_desc_lst, voucher_code_lst, voucher_detail_lst, link)),
                                  columns=['Description', 'Code', 'Details', 'links'])
    return voucher_df