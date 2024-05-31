from concurrent.futures import ThreadPoolExecutor
import csv
import time
import asyncio
import pandas as pd

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import asyncio
from arsenic import get_session, browsers, services


import csv



## Define OPTIONS fr the browser

options = webdriver.ChromeOptions()
options.add_argument("--window-size=1920,1080")
options.add_argument("start-maximized")
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
#options.add_argument('--headless=new')
options.add_argument('--disable-gpu')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--ignore-certificate-errors')
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument('--allow-running-insecure-content')
options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36')


#url = '/groceries/en-GB/products/250037643'
#url2 = f'https://www.tesco.com/{url}'
df = pd.read_csv("Link_List3.csv")


async def scraper(url, limit):
    
    service = services.Chromedriver(binary = r"C:\Users\nuno_\Downloads\chromedriver-win64 (1)\chromedriver-win64\chromedriver.exe")
    browser = browsers.Chrome
    browser.capabilities = {
        'goog:chromeOptions': {"args": ['--disable-gpu', '--no-sandbox', '--disable-dev-shm-usage']}    
        }
    
    async with limit:
        async with get_session(service, browser) as session:
            
            link_list = []
            await session.get(url)
            name = await session.get_attribute('.component__StyledHeading-sc-1t0ixqu-0')
            text_name = await name.get_text()
            #print(text_name)
            link_list.append(text_name)
            link_list_csv = pd.DataFrame(link_list)
            link_list_csv.to_csv('Link_List4.csv', mode='a', index=False, header=False)
#<h1 data-auto="pdp-product-title" class="component__StyledHeading-sc-1t0ixqu-0 kdSqXr ddsweb-heading styled__ProductTitle-mfe-pdp__sc-ebmhjv-6 flNJKr">Tesco Fire Pit 10 Sweet &amp; Smoky Beef Kebabs 400G</h1> 
#<div class="styled__PDPTileContainer-mfe-pdp__sc-ebmhjv-0 cEAseF pdp-tile"><div class="styled__StyledHorizontalTile-sc-1r1v9f3-0 iIJIOq"><section name="image" class="styled__GridSection-mfe-pdp__sc-ebmhjv-1 dBkoTQ"><div class="styled__ImageContainer-mfe-pdp__sc-129esfm-3 bsvrKW"><div class="styled__SashContainer-mfe-pdp__sc-129esfm-7 cdkVRy"><div class="styled__StyledOfferSashList-sc-1hqhl0m-0 ennndX"><span class="styled__StyledContainer-sc-u78h3f-0 guaMyl styled__StyledMarketPlaceTag-sc-1hqhl0m-1 igVacz ddsweb-tag__container">New</span></div></div><picture><img class="styled__Image-sc-j2gwt2-0 llJlgM ddsweb-responsive-image__image" src="https://digitalcontent.api.tesco.com/v2/media/ghs/d9ebc84e-552f-465a-a99f-220f3fd96c5a/dff171c5-8411-4fd1-bd81-e22fdee785ff.jpeg?h=960&amp;w=960" alt="Tesco Fire Pit 10 Sweet &amp; Smoky Beef Kebabs 400G" srcset="https://digitalcontent.api.tesco.com/v2/media/ghs/d9ebc84e-552f-465a-a99f-220f3fd96c5a/dff171c5-8411-4fd1-bd81-e22fdee785ff.jpeg?h=480&amp;w=480 768w, https://digitalcontent.api.tesco.com/v2/media/ghs/d9ebc84e-552f-465a-a99f-220f3fd96c5a/dff171c5-8411-4fd1-bd81-e22fdee785ff.jpeg?h=960&amp;w=960 4000w" aria-label="product Tesco Fire Pit 10 Sweet &amp; Smoky Beef Kebabs 400G" id="carousel__product-image"></picture><button class="styled__StyledIconButton-sc-rnkc1-1 NkjmB styled__ZoomInButton-mfe-pdp__sc-129esfm-2 gpNPXd ddsweb-button ddsweb-button--icon-button" type="button" aria-label="Click here to open zoom in to image"><div class="styled__StyledIconContainer-sc-rnkc1-0 fodRdR"><svg aria-hidden="true" class="styled__SVG-sc-1fqfvah-1 ePjMPv ddsweb-icon__svg" height="21" preserveAspectRatio="xMinYMax meet" viewBox="0 0 21 21" width="21" xmlns="http://www.w3.org/2000/svg" color="currentColor"><path d="M14.5 8a6.5 6.5 0 1 1-13 0 6.5 6.5 0 0 1 13 0zM12.469 12.469l8.03 8.03M5 8h6M8 5v6" fill="none" stroke="#00539f"></path></svg></div></button></div></section><section name="title" class="styled__GridSection-mfe-pdp__sc-ebmhjv-1 bjEIyj"><h1 data-auto="pdp-product-title" class="component__StyledHeading-sc-1t0ixqu-0 kdSqXr ddsweb-heading styled__ProductTitle-mfe-pdp__sc-ebmhjv-6 flNJKr">Tesco Fire Pit 10 Sweet &amp; Smoky Beef Kebabs 400G</h1><div class="styled__ReviewContainer-mfe-pdp__sc-ebmhjv-3 hjCxAg"><a aria-label="This product has an average rating of 3.5 out of 5 star" class="sc-idiyUo cUlEPe ddsweb-star-rating__container" role="group" href="#review-container"><div class="sc-dkzDqf sc-dIouRR jBpzzr dEObwB ddsweb-star-rating__star-container" max="5"><svg aria-hidden="true" class="sc-ftvSup mUvxL sc-fLlhyt jCqNup ddsweb-star-rating__star-icon ddsweb-icon__svg" fill="#fcd700" height="14.67" preserveAspectRatio="xMinYMax meet" stroke="#fcd700" viewBox="0 1 22 22" width="14.67" xmlns="http://www.w3.org/2000/svg" color="#fcd700"><defs><linearGradient id="half-full-ke4vxp"><stop offset="0%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="transparent" stop-opacity="0"></stop><stop offset="100%" stop-color="transparent" stop-opacity="0"></stop></linearGradient></defs><path d="M11 17.05l-5.544 3.07 1.06-6.51L2 8.975l6.237-.955L11 2.12l2.763 5.898L20 8.974l-4.516 4.637 1.06 6.51z" fill="#fcd700" stroke="#fcd700"></path></svg><svg aria-hidden="true" class="sc-ftvSup mUvxL sc-fLlhyt jCqNup ddsweb-star-rating__star-icon ddsweb-icon__svg" fill="#fcd700" height="14.67" preserveAspectRatio="xMinYMax meet" stroke="#fcd700" viewBox="0 1 22 22" width="14.67" xmlns="http://www.w3.org/2000/svg" color="#fcd700"><defs><linearGradient id="half-full-1wouxv"><stop offset="0%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="transparent" stop-opacity="0"></stop><stop offset="100%" stop-color="transparent" stop-opacity="0"></stop></linearGradient></defs><path d="M11 17.05l-5.544 3.07 1.06-6.51L2 8.975l6.237-.955L11 2.12l2.763 5.898L20 8.974l-4.516 4.637 1.06 6.51z" fill="#fcd700" stroke="#fcd700"></path></svg><svg aria-hidden="true" class="sc-ftvSup mUvxL sc-fLlhyt jCqNup ddsweb-star-rating__star-icon ddsweb-icon__svg" fill="#fcd700" height="14.67" preserveAspectRatio="xMinYMax meet" stroke="#fcd700" viewBox="0 1 22 22" width="14.67" xmlns="http://www.w3.org/2000/svg" color="#fcd700"><defs><linearGradient id="half-full-a2i0ke"><stop offset="0%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="transparent" stop-opacity="0"></stop><stop offset="100%" stop-color="transparent" stop-opacity="0"></stop></linearGradient></defs><path d="M11 17.05l-5.544 3.07 1.06-6.51L2 8.975l6.237-.955L11 2.12l2.763 5.898L20 8.974l-4.516 4.637 1.06 6.51z" fill="#fcd700" stroke="#fcd700"></path></svg><svg aria-hidden="true" class="sc-ftvSup mUvxL sc-fLlhyt jCqNup ddsweb-star-rating__star-icon ddsweb-icon__svg" fill="url(#half-full)" height="14.67" preserveAspectRatio="xMinYMax meet" stroke="#fcd700" viewBox="0 1 22 22" width="14.67" xmlns="http://www.w3.org/2000/svg" color="#fcd700"><defs><linearGradient id="half-full-9cqm2e"><stop offset="0%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="transparent" stop-opacity="0"></stop><stop offset="100%" stop-color="transparent" stop-opacity="0"></stop></linearGradient></defs><path d="M11 17.05l-5.544 3.07 1.06-6.51L2 8.975l6.237-.955L11 2.12l2.763 5.898L20 8.974l-4.516 4.637 1.06 6.51z" fill="url(#half-full)" stroke="#fcd700"></path></svg><svg aria-hidden="true" class="sc-ftvSup mUvxL sc-fLlhyt jCqNup ddsweb-star-rating__star-icon ddsweb-icon__svg" fill="#ffffff" height="14.67" preserveAspectRatio="xMinYMax meet" stroke="#cccccc" viewBox="0 1 22 22" width="14.67" xmlns="http://www.w3.org/2000/svg" color="#fcd700"><defs><linearGradient id="half-full-bwrk3d"><stop offset="0%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="#fcd700"></stop><stop offset="50%" stop-color="transparent" stop-opacity="0"></stop><stop offset="100%" stop-color="transparent" stop-opacity="0"></stop></linearGradient></defs><path d="M11 17.05l-5.544 3.07 1.06-6.51L2 8.975l6.237-.955L11 2.12l2.763 5.898L20 8.974l-4.516 4.637 1.06 6.51z" fill="#ffffff" stroke="#cccccc"></path></svg></div><span class="text__StyledText-sc-1jpzi8m-0 dyJCjQ ddsweb-text sc-dmRaPn ijaJht ddsweb-star-rating__average-rating-text">3.5</span><span class="text__StyledText-sc-1jpzi8m-0 dyJCjQ ddsweb-text sc-hHLeRK hAoriC ddsweb-star-rating__ratings-count">(2)</span></a><div class="styled__WriteAReviewContainer-mfe-pdp__sc-ebmhjv-4 eGGISz"><a class="styled__Anchor-sc-1i711qa-0 cVyEAP styled__StyledLink-sc-k2gmo0-0 eNCmkU ddsweb-link__anchor" href="https://www.tesco.com/groceries/en-GB/reviews/submission/313605866?from=/products/313605866"><span class="styled__Text-sc-1i711qa-1 edtCHn ddsweb-link__text">Write a review</span><span class="styled__IconContainer-sc-1i711qa-2 dpYbaI ddsweb-link__icon-container"><svg aria-hidden="true" class="styled__SVG-sc-1fqfvah-1 ePjMPv ddsweb-link__icon ddsweb-icon__svg" height="10" preserveAspectRatio="xMinYMax meet" viewBox="-1 0 12 20" width="6" xmlns="http://www.w3.org/2000/svg" color="currentColor"><path d="M1.312 1.348L10.276 10l-8.964 8.644" fill="none" stroke="currentColor"></path></svg></span></a></div></div><div class="styled__Details-mfe-pdp__sc-ebmhjv-7 dqYwFc"><div class="styled__PromotionsContainer-sc-nc07d4-3 eHwhpv"><div><div class="styled__StyledPromotionsWithClubcardPriceContainer-sc-dfqdes-0 fPCGKx"><a href="/groceries/en-GB/promotions/89916144" class="styled__Container-sc-1d7lp92-4 hUMuNo ddsweb-value-bar__container"><div class="styled__InnerContainer-sc-1d7lp92-5 bLPMhL ddsweb-value-bar__inner-container"><div class="styled__ClubcardPriceLogo-sc-1d7lp92-6 fzdbrq ddsweb-value-bar__clubcard-logo"><svg role="img" width="56" height="56" fill="none" xmlns="http://www.w3.org/2000/svg"><title>Clubcard Price</title><path d="M0 12C0 5.373 5.373 0 12 0h44v56H12C5.373 56 0 50.627 0 44V12Z" fill="#00539F"></path><path d="M10.315 27.08c-.6 0-1.157-.137-1.67-.41a3.185 3.185 0 0 1-1.24-1.23c-.313-.547-.47-1.193-.47-1.94 0-.747.157-1.39.47-1.93a3.097 3.097 0 0 1 1.24-1.23c.513-.28 1.07-.42 1.67-.42.727 0 1.344.17 1.85.51.514.34.874.827 1.08 1.46l-1.13.45a1.638 1.638 0 0 0-.64-.88c-.306-.227-.693-.34-1.16-.34-.373 0-.717.09-1.03.27a1.86 1.86 0 0 0-.75.8c-.187.353-.28.79-.28 1.31s.093.96.28 1.32c.187.353.437.62.75.8.313.173.657.26 1.03.26.467 0 .854-.11 1.16-.33.314-.22.527-.517.64-.89l1.13.45c-.206.633-.566 1.12-1.08 1.46-.506.34-1.123.51-1.85.51Zm5.153-.08h-1.24v-7.08h1.24V27Zm5.927 0h-1.24v-.81c-.174.28-.397.5-.67.66-.274.153-.577.23-.91.23-.547 0-.974-.163-1.28-.49-.3-.327-.45-.777-.45-1.35v-3.4h1.24v3.1c0 .667.29 1 .87 1 .38 0 .673-.163.88-.49.213-.333.32-.787.32-1.36v-2.25h1.24V27Zm4.156.08a1.99 1.99 0 0 1-.9-.19 1.503 1.503 0 0 1-.58-.51V27h-1.24v-7.08h1.24v2.55c.167-.22.38-.393.64-.52s.55-.19.87-.19c.44 0 .83.113 1.17.34.34.227.604.543.79.95.194.4.29.857.29 1.37 0 .507-.103.963-.31 1.37-.2.4-.473.717-.82.95-.346.227-.73.34-1.15.34Zm-.28-1.14c.367 0 .67-.137.91-.41.247-.273.37-.643.37-1.11 0-.467-.123-.837-.37-1.11a1.159 1.159 0 0 0-.91-.41 1.19 1.19 0 0 0-.92.41c-.24.273-.36.643-.36 1.11 0 .467.12.837.36 1.11.247.273.554.41.92.41Zm6.08 1.14c-.507 0-.957-.113-1.35-.34-.394-.227-.7-.54-.92-.94a2.853 2.853 0 0 1-.33-1.38c0-.513.11-.97.33-1.37.22-.407.526-.723.92-.95.393-.227.843-.34 1.35-.34 1.146 0 1.923.47 2.33 1.41l-1.13.51c-.26-.52-.66-.78-1.2-.78-.387 0-.707.14-.96.42-.254.28-.38.647-.38 1.1 0 .453.126.82.38 1.1.253.28.573.42.96.42.54 0 .94-.26 1.2-.78l1.13.51c-.407.94-1.184 1.41-2.33 1.41Zm4.666 0c-.3 0-.583-.06-.85-.18a1.538 1.538 0 0 1-.64-.52c-.16-.233-.24-.51-.24-.83 0-.507.19-.913.57-1.22.38-.313.894-.47 1.54-.47h1.11v-.18c0-.26-.09-.467-.27-.62-.18-.16-.423-.24-.73-.24-.246 0-.47.067-.67.2-.2.127-.35.277-.45.45l-.95-.57c.18-.327.447-.597.8-.81.354-.22.777-.33 1.27-.33.707 0 1.257.17 1.65.51.394.34.59.83.59 1.47V27h-1.02l-.17-.66c-.166.227-.38.407-.64.54-.253.133-.553.2-.9.2Zm.3-1.06c.334 0 .614-.1.84-.3.234-.2.35-.447.35-.74v-.14h-.98c-.286 0-.516.057-.69.17a.506.506 0 0 0-.25.45c0 .18.06.32.18.42.127.093.31.14.55.14Zm3.653-4.18h1.24v.78c.147-.28.353-.493.62-.64.267-.147.563-.22.89-.22.34 0 .607.077.8.23l-.42 1.05a1.144 1.144 0 0 0-.55-.14c-.387 0-.707.167-.96.5-.253.333-.38.847-.38 1.54V27h-1.24v-5.16ZM46 27.08c-.42 0-.803-.113-1.15-.34a2.337 2.337 0 0 1-.82-.95 3.15 3.15 0 0 1-.29-1.37c0-.513.094-.97.28-1.37.194-.407.46-.723.8-.95.34-.227.73-.34 1.17-.34.347 0 .65.063.91.19.26.12.46.293.6.52v-2.55h1.24V27H47.5v-.62a1.676 1.676 0 0 1-.6.51 1.99 1.99 0 0 1-.9.19Zm.3-1.14c.367 0 .67-.137.91-.41.248-.273.37-.643.37-1.11 0-.467-.122-.837-.37-1.11a1.159 1.159 0 0 0-.91-.41c-.366 0-.672.137-.92.41-.24.273-.36.643-.36 1.11 0 .467.12.837.36 1.11.247.273.554.41.92.41ZM17.957 37h-1.3v-7h2.57c.467 0 .87.097 1.21.29.34.187.6.447.78.78.18.327.27.693.27 1.1 0 .407-.09.777-.27 1.11-.18.327-.44.587-.78.78-.34.187-.743.28-1.21.28h-1.27V37Zm1.17-3.86c.32 0 .574-.08.76-.24.187-.167.28-.41.28-.73s-.093-.56-.28-.72c-.186-.167-.44-.25-.76-.25h-1.17v1.94h1.17Zm3.359-1.3h1.24v.78c.146-.28.353-.493.62-.64.266-.147.563-.22.89-.22.34 0 .606.077.8.23l-.42 1.05a1.144 1.144 0 0 0-.55-.14c-.387 0-.707.167-.96.5-.254.333-.38.847-.38 1.54V37h-1.24v-5.16Zm4.187-1.34c0-.227.076-.417.23-.57a.774.774 0 0 1 .57-.23c.226 0 .416.077.57.23.153.153.23.343.23.57a.774.774 0 0 1-.23.57.774.774 0 0 1-.57.23.774.774 0 0 1-.57-.23.774.774 0 0 1-.23-.57Zm1.42 6.5h-1.24v-5.16h1.24V37Zm3.723.08c-.507 0-.957-.113-1.35-.34-.394-.227-.7-.54-.92-.94a2.853 2.853 0 0 1-.33-1.38c0-.513.11-.97.33-1.37.22-.407.526-.723.92-.95.393-.227.843-.34 1.35-.34 1.146 0 1.923.47 2.33 1.41l-1.13.51c-.26-.52-.66-.78-1.2-.78-.387 0-.707.14-.96.42-.254.28-.38.647-.38 1.1 0 .453.126.82.38 1.1.253.28.573.42.96.42.54 0 .94-.26 1.2-.78l1.13.51c-.407.94-1.184 1.41-2.33 1.41Zm8.026-2.26h-3.81c.067.38.224.67.47.87.247.193.547.29.9.29.294 0 .537-.06.73-.18.2-.127.39-.317.57-.57l1.05.57c-.253.413-.576.73-.97.95-.386.22-.87.33-1.45.33-.546 0-1.016-.127-1.41-.38a2.463 2.463 0 0 1-.87-1 2.945 2.945 0 0 1-.29-1.28c0-.447.1-.873.3-1.28.207-.407.504-.737.89-.99.387-.26.844-.39 1.37-.39.534 0 .99.12 1.37.36.38.24.667.557.86.95.194.387.29.8.29 1.24v.51Zm-1.27-.98a1.134 1.134 0 0 0-.41-.72c-.22-.187-.5-.28-.84-.28-.286 0-.543.09-.77.27a1.333 1.333 0 0 0-.47.73h2.49Z" fill="#fff"></path></svg></div><div class="styled__ContentContainer-sc-1d7lp92-7 hlqvAA ddsweb-value-bar__content-container"><p class="text__StyledText-sc-1jpzi8m-0 eifUHO ddsweb-text styled__ContentText-sc-1d7lp92-8 bWtqaA ddsweb-value-bar__content-text">Any 2 for £8 Clubcard Price - Selected Tesco Ready To Cook &amp; Bbq Products 250g-1120g</p></div><div class="styled__IconContainer-sc-1d7lp92-11 gNtzDq ddsweb-value-bar__icon-container"><svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="none" aria-hidden="true"><path d="M4.354 2.771 9.77 8l-5.417 5.223 1.04 1.08L11.932 8 5.395 1.692l-1.041 1.08Z" fill="#00539F"></path></svg></div></div><p class="text__StyledText-sc-1jpzi8m-0 edBSUG ddsweb-text styled__TermsText-sc-1d7lp92-9 ialCTG ddsweb-value-bar__terms">Offer valid for delivery from 25/03/2024 until 22/09/2024</p></a></div></div></div><div data-auto="pdp-buy-box" class="styled__BuyBoxContainer-mfe-pdp__sc-ebmhjv-5 hkkbie"><div class="base-components__RootElement-sc-150pv2j-1 styled__Container-sc-159tobh-0 hjMZDF gUZlYv ddsweb-buybox__container"><div class="base-components__BaseElement-sc-150pv2j-0 styled__PriceAndActions-sc-159tobh-3 chGOgR bgcAqA ddsweb-buybox__price-and-actions"><div class="styled__StyledPriceContainer-sc-159tobh-5 fPFdvw"><div class="base-components__RootElement-sc-150pv2j-1 styled__Container-sc-v0qv7n-0 hjMZDF gVxPxM ddsweb-buybox__price ddsweb-price__container"><p class="text__StyledText-sc-1jpzi8m-0 lmgzsH ddsweb-text styled__PriceText-sc-v0qv7n-1 eNIEDh">£5.00</p><p class="text__StyledText-sc-1jpzi8m-0 dyJCjQ ddsweb-text styled__Subtext-sc-v0qv7n-2 nsITR ddsweb-price__subtext">£12.50/kg</p></div></div><div class="base-components__RootElement-sc-150pv2j-1 styled__Container-sc-195yncy-0 hjMZDF juMmIu ddsweb-buybox__actions ddsweb-quantity-controls__container"><div class="base-components__RootElement-sc-150pv2j-1 styled__Container-sc-1rbigln-0 hjMZDF lklIVe styled__StyledFormGroup-sc-195yncy-1 ffCFpg ddsweb-quantity-controls__form-group ddsweb-form-group__container"><label class="styled__StyledLabel-sc-1bpek9-0 hUYHO styled__StyledLabel-sc-1rbigln-2 kxGWYE ddsweb-form-group__label ddsweb-label" for="quantity-controls-313605866">Quantity controls, undefined</label><div class="base-components__BaseElement-sc-150pv2j-0 styled__Children-sc-1rbigln-5 chGOgR fOHpBv ddsweb-form-group__children"><div class="styled__StyledQuantityControlWrapper-sc-195yncy-6 jwCMAF"><label id="quantity-controls-313605866-label" class="styled__VisuallyHiddenLabel-sc-195yncy-7 gLGqxl">Quantity of Tesco Fire Pit 10 Sweet &amp; Smoky Beef Kebabs 400G</label><div class="component__Wrapper-sc-19wd3h0-3 hwNxcz input-wrapper"><input type="number" class="base-components__RootElement-sc-150pv2j-1 styled__StyledInput-sc-7h0jvk-0 component__StyledAsInput-sc-19wd3h0-4 hjMZDF boQttd styled__StyledInput-sc-195yncy-3 kIwOxn ddsweb-quantity-controls__input ddsweb-input" data-auto="ddsweb-quantity-controls-input" autocomplete="off" id="quantity-controls-313605866" maxlength="2" aria-labelledby="quantity-controls-313605866-label" value="1"></div></div><button class="styled__StyledTextButton-sc-8hxn3m-0 YGUEZ styled__StyledButton-sc-195yncy-5 irnfGg ddsweb-quantity-controls__add-button ddsweb-button ddsweb-button--text-button" type="submit" data-auto="ddsweb-quantity-controls-add-button" aria-label="add 1 Tesco Fire Pit 10 Sweet &amp; Smoky Beef Kebabs 400G"><span class="shared-containers__StyledInnerContainer-sc-93ev6e-2 dBfzGT ddsweb-button__inner-container">Add</span></button></div></div></div></div></div></div><div data-auto="pdp-product-tile-messaging" class="styled__StyledMessaging-mfe-pdp__sc-ebmhjv-9 eBmNng"><span></span><span></span></div></div></section></div></div>



async def run():
    
    limit = asyncio.Semaphore(10)
    
    for x in df['0']:
        url = f'https://www.tesco.com/{x}'
        
        await scraper(url, limit)
  
  
asyncio.run(run())