import pytest

from app.lib.mapper.sch_mapper import map_home


def test_map_home():
    aem_content = {
        "schPagev1ByPath": {
            "item": {
                "_path": "/content/dam/decd-endc/content-fragments/sch/pages/my-dashboard",
                "scPageNameEn": "my-dashboard",
                "scPageNameFr": "mon-tableau-de-bord",
                "scTitleEn": "My dashboard",
                "scTitleFr": "Mon tableau de bord",
                "scBreadcrumbParentPages": [],
                "scContentType": ["gc:content-types/navigation-page"],
                "scOwner": ["gc:institutions/service-canada"],
                "scDateModifiedOverwrite": "2022-10-17T12:51:30.000-04:00",
                "scFragments": [
                    {
                        "scId": "exit-beta-version",
                        "scTitleEn": "Exit Beta version",
                        "scTitleFr": "Quitter la version beta",
                        "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/view-change.shtml",
                        "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/visualiser-modifier.shtml",
                    },
                    {
                        "scId": "dashboard-cards",
                        "scItems": [
                            {
                                "scId": "employment-insurance",
                                "scTitleEn": "Employment Insurance",
                                "scTitleFr": "Assurance-emploi",
                                "schLists": [
                                    {
                                        "scTitleEn": "Most requested",
                                        "scTitleFr": "En demande",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my Employment Insurance status updates",
                                                "scTitleFr": "Consulter l'état de ma demande d'assurance-emploi",
                                                "scDestinationURLEn": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scDestinationURLFr": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scIconCSS": "list-check",
                                            },
                                            {
                                                "scTitleEn": "View my Employment Insurance payments",
                                                "scTitleFr": "Voir mes paiements d'assurance-emploi",
                                                "scDestinationURLEn": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scDestinationURLFr": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scIconCSS": "file-invoice-dollar",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Applications",
                                        "scTitleFr": "Demandes de prestations",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my Employment Insurance status updates",
                                                "scTitleFr": "Consulter l'état de ma demande d'assurance-emploi",
                                                "scDestinationURLEn": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scDestinationURLFr": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scIconCSS": "list-check",
                                            },
                                            {
                                                "scTitleEn": "Apply for Employment Insurance",
                                                "scTitleFr": "Présenter une demande d'assurance-emploi",
                                                "scDestinationURLEn": "https://www.canada.ca/en/services/benefits/ei/ei-regular-benefit/apply.html#gc-document-nav",
                                                "scDestinationURLFr": "https://www.canada.ca/fr/services/prestations/ae/assurance-emploi-reguliere/demande.html",
                                                "scIconCSS": "stamp",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Payments and claims",
                                        "scTitleFr": "Paiements et demandes",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my Employment Insurance payments",
                                                "scTitleFr": "Voir mes paiements d'assurance-emploi",
                                                "scDestinationURLEn": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scDestinationURLFr": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                                "scIconCSS": "file-invoice-dollar",
                                            },
                                            {
                                                "scTitleEn": "View my latest Employment Insurance claim",
                                                "scTitleFr": "Consulter ma dernière demande d'assurance-emploi",
                                                "scDestinationURLEn": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/dashboard",
                                                "scDestinationURLFr": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/fr/dashboard",
                                                "scIconCSS": "file-signature",
                                            },
                                            {
                                                "scTitleEn": "View my past Employment Insurance claims",
                                                "scTitleFr": "Consulter mes demandes antérieures d'assurance-emploi",
                                                "scDestinationURLEn": "https://www.canada.ca/en/employment-social-development/corporate/portfolio/service-canada.html",
                                                "scDestinationURLFr": "https://www.canada.ca/en/employment-social-development/corporate/portfolio/service-canada.html",
                                                "scIconCSS": "briefcase",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Taxes",
                                        "scTitleFr": "Impôts",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my tax slips",
                                                "scTitleFr": "Consulter mes feuillets d'impôt",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/tiso/view-tax-slips.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/frfd/visualiser-feuillets-renseignement-fiscaux.shtml",
                                                "scIconCSS": "receipt",
                                            },
                                            {
                                                "scTitleEn": "Change my tax slip delivery options",
                                                "scTitleFr": "Modifier mes options d'expédition des feuillets d'impôt",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/m sca/cpp-oas/tiso/delivery/change.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/frfd/mode-livraison/modifier.shtml",
                                                "scIconCSS": "envelope-open-text",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Reports and documents",
                                        "scTitleFr": "Rapports et documents",
                                        "scItems": [
                                            {
                                                "scTitleEn": "Complete my Employment Insurance report",
                                                "scTitleFr": "Soumettre une déclaration de l'assurance- emploi",
                                                "scDestinationURLEn": "https://www.canada.ca/en/services/benefits/ei/employment-insurance-reporting.html",
                                                "scDestinationURLFr": "https://www.canada.ca/fr/services/prestations/ae/declarations-assurance-emploi.html",
                                                "scIconCSS": "pen-to-square",
                                            },
                                            {
                                                "scTitleEn": "View my records of employment",
                                                "scTitleFr": "Consulter mes relevés d'emploi",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/roe/view.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/re/visionner.shtml",
                                                "scIconCSS": "file-contract",
                                            },
                                            {
                                                "scTitleEn": "View my Employment Insurance documents",
                                                "scTitleFr": "Consulter mes documents d'assurance-emploi",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/dus/view.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/td/voir.shtml",
                                                "scIconCSS": "folder-open",
                                            },
                                            {
                                                "scTitleEn": "View my Employment Insurance letters",
                                                "scTitleFr": "Consulter mes lettres d'assurance-emploi",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/dol/view.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/adl/voir.shtml",
                                                "scIconCSS": "envelopes-bulk",
                                            },
                                            {
                                                "scTitleEn": "Submit documents for Employment Insurance",
                                                "scTitleFr": "Soumettre des documents pour l'assurance-emploi",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/dus/instructions.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/td/instructions.shtml",
                                                "scIconCSS": "file-import",
                                            },
                                            {
                                                "scTitleEn": "Submit eForms for Employment Insurance",
                                                "scTitleFr": "Soumettre des formulaires électroniques pour l'assurance-emploi",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/eforms/landing.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/formulaires-en-ligne/accueil.shtml",
                                                "scIconCSS": "laptop-file",
                                            },
                                            {
                                                "scTitleEn": "Report a mistake",
                                                "scTitleFr": "Communiquer une erreur",
                                                "scDestinationURLEn": "https://www.canada.ca/en/services/benefits/ei/ei-regular-benefit/while-receiving.html#h2.08",
                                                "scDestinationURLFr": "https://www.canada.ca/fr/services/prestations/ae/assurance-emploi-reguliere/pendant-que-vous-recevez.html#h2.08",
                                                "scIconCSS": "file-exclamation",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Personal information",
                                        "scTitleFr": "Renseignements personnels",
                                        "scItems": [
                                            {
                                                "scTitleEn": "Update my profile",
                                                "scTitleFr": "Mettre à jour mon profil",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/contact-information/landing.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/renseignements-personnels/accueil.shtml",
                                                "scIconCSS": "circle-user",
                                            },
                                            {
                                                "scTitleEn": "Manage email notifications (Alert me)",
                                                "scTitleFr": "Gérer mes avis par courriel (Alertez-moi)",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/alert-me/submit.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/alertez-moi/soumettre.shtml",
                                                "scIconCSS": "bell",
                                            },
                                            {
                                                "scTitleEn": "Get my access code",
                                                "scTitleFr": "Consulter mon code d'accès",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/access-code.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/code-acces.shtml",
                                                "scIconCSS": "key",
                                            },
                                            {
                                                "scTitleEn": "View my agreement status (self-employed) for Employment Insurance",
                                                "scTitleFr": "Consulter l'état de mon entente (travailleurs autonomes) pour l'assurance-emploi",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/self-employment/current-status.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/travailleur-autonome/etat-actuel.shtml",
                                                "scIconCSS": "person-walking-luggage",
                                            },
                                        ],
                                    },
                                ],
                            },
                            {
                                "scId": "canada-pension-plan",
                                "scTitleEn": "Canada Pension Plan",
                                "scTitleFr": "Régime de pensions du Canada",
                                "schLists": [
                                    {
                                        "scTitleEn": "Most requested",
                                        "scTitleFr": "En demande",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my status updates for Canada Pension Plan",
                                                "scTitleFr": "Consulter l'état de ma demande pour le Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/ved/choisissez.shtml",
                                                "scIconCSS": "list-check",
                                            },
                                            {
                                                "scTitleEn": "View my Canada Pension Plan and Old Age Security payments ",
                                                "scTitleFr": "Consulter mes paiements du Régime de pensions du Canada et de la Sécurité de la vieillesse",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/vmrp/renseignements-paiement/details.shtml",
                                                "scIconCSS": "file-invoice-dollar",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Applications",
                                        "scTitleFr": "Demandes de prestations",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my status updates for Canada Pension Plan",
                                                "scTitleFr": "Consulter l'état de ma demande pour le Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/ved/choisissez.shtml",
                                                "scIconCSS": "list-check",
                                            },
                                            {
                                                "scTitleEn": "Apply for Canada Pension Plan",
                                                "scTitleFr": "Présenter une demande au Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/rtr-applicaton/step1-apply.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/demande-ret/etape1-presenter-demande.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                            {
                                                "scTitleEn": "Apply for Canada Pension Plan Disability",
                                                "scTitleFr": "Présenter une demande de prestations d'invalidité du Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/ccpd-applicaton/application-in-progress.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/demande-pirpc/demande-en-cours.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                            {
                                                "scTitleEn": " Apply for Canada Pension Plan Death Benefits",
                                                "scTitleFr": "Présenter une demande pour prestations de décès du Régime de pensions du Canada ",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/cpp-death-benefits-general.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/rpc-prestations-deces-general.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                            {
                                                "scTitleEn": "Apply for Canada Pension Plan Survivor's Pension and Children's Benefit",
                                                "scTitleFr": "Présenter une demande pour la pension de survivant du Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/survivor-children-benefits/general-information.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/survivant-enfant/renseignements-generaux.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                            {
                                                "scTitleEn": "Apply for Canada Pension Plan Survivor's Pension and Children's Benefit aged 18 to 25",
                                                "scTitleFr": "Présenter une demande de prestations d'enfant de 18 à 25 ans du Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/child-benefits/general-information.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/prestation-enfant/renseignements-generaux.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Payments",
                                        "scTitleFr": "Paiements",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my Canada Pension Plan and Old Age Security payments ",
                                                "scTitleFr": "Consulter mes paiements du Régime de pensions du Canada et de la Sécurité de la vieillesse",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/vmrp/renseignements-paiement/details.shtml",
                                                "scIconCSS": "file-invoice-dollar",
                                            },
                                            {
                                                "scTitleEn": "View my Canada Pension Plan contributions",
                                                "scTitleFr": "Consulter mes cotisations au Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/soc/earnings-contributions.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/ecc/gains-cotisations.shtml",
                                                "scIconCSS": "hand-holding-dollar",
                                            },
                                            {
                                                "scTitleEn": "Estimate my retirement income for Canada Pension Plan",
                                                "scTitleFr": "Estimer mon revenu de retraite pour le Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/soc/estimated-benefits.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/ecc/estimation-prestations.shtml",
                                                "scIconCSS": "calculator",
                                            },
                                            {
                                                "scTitleEn": "Request a review of a decision for Canada Pension Plan",
                                                "scTitleFr": "Faire une demande de révision pour le Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/request-reconsideration/step1-information-about-you.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/demande-reexamen/etape1-renseignements-sujet.shtml",
                                                "scIconCSS": "comments",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Taxes",
                                        "scTitleFr": "Impôts",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my tax slips",
                                                "scTitleFr": "Consulter mes feuillets d'impôt",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/tiso/view-tax-slips.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/frfd/visualiser-feuillets-renseignement-fiscaux.shtml",
                                                "scIconCSS": "receipt",
                                            },
                                            {
                                                "scTitleEn": "Change my tax deductions for the Canada Pension Plan",
                                                "scTitleFr": "Modifier ma retenue d'impôts pour le Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/fvtd/start.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/rvif/appliquer.shtml",
                                                "scIconCSS": "arrow-down-wide-short",
                                            },
                                            {
                                                "scTitleEn": "Change my tax slip delivery options",
                                                "scTitleFr": "Modifier mes options d'expédition des feuillets d'impôt",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/m sca/cpp-oas/tiso/delivery/change.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/frfd/mode-livraison/modifier.shtml",
                                                "scIconCSS": "envelope-open-text",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Documents",
                                        "scTitleFr": "Documents",
                                        "scItems": [
                                            {
                                                "scTitleEn": "Submit documents for Canada Pension Plan Disability",
                                                "scTitleFr": "Soumettre des documents pour les prestations d'invalidité du Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/dus/step1-select-document.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/td/etape1-selectionnez-document.shtml",
                                                "scIconCSS": "file-import",
                                            },
                                            {
                                                "scTitleEn": "Submit a declaration of attendance at school or university",
                                                "scTitleFr": "Soumettre une déclaration de fréquentation scolaire ou universitaire",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/declaration-attendance-school/step1-information-enrolment.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/declaration-frequentation-scolaire/etape1-information-inscription.shtml",
                                                "scIconCSS": "school",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Provisions",
                                        "scTitleFr": "Clauses",
                                        "scItems": [
                                            {
                                                "scTitleEn": "Request child-rearing provisions",
                                                "scTitleFr": "Demander une clause pour élever des enfants",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/crp/request-crp.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/cee/demander-cee.shtml",
                                                "scIconCSS": "baby-carriage",
                                            },
                                            {
                                                "scTitleEn": "View my child-rearing provision",
                                                "scTitleFr": "Consulter ma clause pour élever des enfants",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/crp/crp-information-with-children-option1.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/cee/renseignements-cee-avec-enfants-option1.shtml",
                                                "scIconCSS": "baby-carriage",
                                            },
                                            {
                                                "scTitleEn": "Apply for Canada Pension Plan credit split",
                                                "scTitleFr": "Demander de partager des crédits du Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/cpp-credit-split/general-information.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/partage-credits/renseignements-generaux.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                            {
                                                "scTitleEn": "Apply for Canada Pension Plan sharing ",
                                                "scTitleFr": "Demander de partager des pensions de retraite du Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/cpp-pension-sharing/general-info.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/rpc-partage-pensions/renseignements-generaux.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Personal information",
                                        "scTitleFr": "Renseignements personnels",
                                        "scItems": [
                                            {
                                                "scTitleEn": "Update my profile",
                                                "scTitleFr": "Mettre à jour mon profil",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/contact-information/landing.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/renseignements-personnels/accueil.shtml",
                                                "scIconCSS": "circle-user",
                                            },
                                            {
                                                "scTitleEn": "Give consent to communicate on my behalf",
                                                "scTitleFr": "Autoriser une personne à communiquer en mon nom",
                                                "scDestinationURLEn": "https://catalogue.servicecanada.gc.ca/content/EForms/en/Detail.html?Form=INS3280",
                                                "scDestinationURLFr": "https://catalogue.servicecanada.gc.ca/content/EForms/fr/Detail.html?Form=INS3280",
                                                "scIconCSS": "user-check",
                                            },
                                        ],
                                    },
                                ],
                            },
                            {
                                "scId": "old-age-security",
                                "scTitleEn": "Old Age Security",
                                "scTitleFr": "Sécurité de la vieillesse",
                                "schLists": [
                                    {
                                        "scTitleEn": "Most requested",
                                        "scTitleFr": "En demande",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my Old Age Security status updates ",
                                                "scTitleFr": "Consulter l'état de ma demande de pension de la Sécurité de la vieillesse",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/ved/choisissez.shtml",
                                                "scIconCSS": "list-check",
                                            },
                                            {
                                                "scTitleEn": "View my Canada Pension Plan and Old Age Security payments ",
                                                "scTitleFr": "Consulter mes paiements du Régime de pensions du Canada et de la Sécurité de la vieillesse",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/vmrp/renseignements-paiement/details.shtml",
                                                "scIconCSS": "file-invoice-dollar",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Applications",
                                        "scTitleFr": "Demandes de prestations",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my Old Age Security status updates ",
                                                "scTitleFr": "Consulter l'état de ma demande de pension de la Sécurité de la vieillesse",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/ved/choisissez.shtml",
                                                "scIconCSS": "list-check",
                                            },
                                            {
                                                "scTitleEn": "Apply for Old Age Security and Guaranteed Income Supplement",
                                                "scTitleFr": "Présenter une demande pour la Pension de la Sécurité de la vieillesse et le Supplément  de revenu garanti",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/oas-gis-application/choose.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/demande-sv-srg/choisissez.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                            {
                                                "scTitleEn": "Apply for Guaranteed Income Supplement",
                                                "scTitleFr": "Présenter une demande pour le Supplément de revenu de garanti",
                                                "scDestinationURLEn": "https://www.canada.ca/en/services/benefits/publicpensions/cpp/old-age-security/guaranteed-income-supplement/apply.html",
                                                "scDestinationURLFr": "https://www.canada.ca/fr/services/prestations/pensionspubliques/rpc/securite-vieillesse/supplement-revenu-garanti/demande.html",
                                                "scIconCSS": "stamp",
                                            },
                                            {
                                                "scTitleEn": "Apply for Allowance or Allowance for the Survivor",
                                                "scTitleFr": "Présenter une demande d'Allocation ou d'Allocation au survivant",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/alw-alws/general-information.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/alc-alcs/informations-generales.shtml",
                                                "scIconCSS": "stamp",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Payments",
                                        "scTitleFr": "Paiements",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my Canada Pension Plan and Old Age Security payments ",
                                                "scTitleFr": "Consulter mes paiements du Régime de pensions du Canada et de la Sécurité de la vieillesse",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/vmrp/renseignements-paiement/details.shtml",
                                                "scIconCSS": "file-invoice-dollar",
                                            },
                                            {
                                                "scTitleEn": "Delay receiving Old Age Security",
                                                "scTitleFr": "Reporter le début de ma pension",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/delay-oas-gis/choose.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/vmrp/reporter-sv-srg/choisissez.shtml",
                                                "scIconCSS": "clock-rotate-left",
                                            },
                                            {
                                                "scTitleEn": "Estimate my retirement income for Old Age Security",
                                                "scTitleFr": "Estimer mon revenu de retraite pour la Sécurité de la vieillesse",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/soc/estimated-benefits.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/ecc/estimation-prestations.shtml",
                                                "scIconCSS": "calculator",
                                            },
                                            {
                                                "scTitleEn": "Request a review of a decision for Canada Pension Plan",
                                                "scTitleFr": "Faire une demande de révision pour le Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/request-reconsideration/step1-information-about-you.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/demande-reexamen/etape1-renseignements-sujet.shtml",
                                                "scIconCSS": "comments",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Taxes",
                                        "scTitleFr": "Impôts",
                                        "scItems": [
                                            {
                                                "scTitleEn": "View my tax slips",
                                                "scTitleFr": "Consulter mes feuillets d'impôt",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/tiso/view-tax-slips.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/frfd/visualiser-feuillets-renseignement-fiscaux.shtml",
                                                "scIconCSS": "receipt",
                                            },
                                            {
                                                "scTitleEn": "Change my tax deductions for the Canada Pension Plan",
                                                "scTitleFr": "Modifier ma retenue d'impôts pour le Régime de pensions du Canada",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/fvtd/start.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/rvif/appliquer.shtml",
                                                "scIconCSS": "arrow-down-wide-short",
                                            },
                                            {
                                                "scTitleEn": "Change my tax slip delivery options",
                                                "scTitleFr": "Modifier mes options d'expédition des feuillets d'impôt",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/m sca/cpp-oas/tiso/delivery/change.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/rpc-sv/frfd/mode-livraison/modifier.shtml",
                                                "scIconCSS": "envelope-open-text",
                                            },
                                        ],
                                    },
                                    {
                                        "scTitleEn": "Personal information",
                                        "scTitleFr": "Renseignements personnels",
                                        "scItems": [
                                            {
                                                "scTitleEn": "Update my profile",
                                                "scTitleFr": "Mettre à jour mon profil",
                                                "scDestinationURLEn": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/contact-information/landing.shtml",
                                                "scDestinationURLFr": "https://esdc.prv/fr/service-canada/prestation-services/assistance-aps/mdsc/ae/renseignements-personnels/accueil.shtml",
                                                "scIconCSS": "circle-user",
                                            },
                                            {
                                                "scTitleEn": "Give consent to communicate on my behalf",
                                                "scTitleFr": "Autoriser une personne à communiquer en mon nom",
                                                "scDestinationURLEn": "https://catalogue.servicecanada.gc.ca/content/EForms/en/Detail.html?Form=INS3280",
                                                "scDestinationURLFr": "https://catalogue.servicecanada.gc.ca/content/EForms/fr/Detail.html?Form=INS3280",
                                                "scIconCSS": "user-check",
                                            },
                                        ],
                                    },
                                ],
                            },
                        ],
                    },
                ],
            }
        }
    }

    mapped_content = map_home(aem_content)
    assert mapped_content == {
        "title": "My dashboard",
        "cards": [
            {
                "id": "employment-insurance",
                "title": "Employment Insurance",
                "lists": [
                    {
                        "title": "Most requested",
                        "tasks": [
                            {
                                "title": "View my Employment Insurance status updates",
                                "link": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                "icon": "list-check",
                            },
                            {
                                "title": "View my Employment Insurance payments",
                                "link": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                "icon": "file-invoice-dollar",
                            },
                        ],
                    },
                    {
                        "title": "Applications",
                        "tasks": [
                            {
                                "title": "View my Employment Insurance status updates",
                                "link": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                "icon": "list-check",
                            },
                            {
                                "title": "Apply for Employment Insurance",
                                "link": "https://www.canada.ca/en/services/benefits/ei/ei-regular-benefit/apply.html#gc-document-nav",
                                "icon": "stamp",
                            },
                        ],
                    },
                    {
                        "title": "Payments and claims",
                        "tasks": [
                            {
                                "title": "View my Employment Insurance payments",
                                "link": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/",
                                "icon": "file-invoice-dollar",
                            },
                            {
                                "title": "View my latest Employment Insurance claim",
                                "link": "https://sc-digital-centre-dev.bdm-dev.dts-stn.com/dashboard",
                                "icon": "file-signature",
                            },
                            {
                                "title": "View my past Employment Insurance claims",
                                "link": "https://www.canada.ca/en/employment-social-development/corporate/portfolio/service-canada.html",
                                "icon": "briefcase",
                            },
                        ],
                    },
                    {
                        "title": "Taxes",
                        "tasks": [
                            {
                                "title": "View my tax slips",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/tiso/view-tax-slips.shtml",
                                "icon": "receipt",
                            },
                            {
                                "title": "Change my tax slip delivery options",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/m sca/cpp-oas/tiso/delivery/change.shtml",
                                "icon": "envelope-open-text",
                            },
                        ],
                    },
                    {
                        "title": "Reports and documents",
                        "tasks": [
                            {
                                "title": "Complete my Employment Insurance report",
                                "link": "https://www.canada.ca/en/services/benefits/ei/employment-insurance-reporting.html",
                                "icon": "pen-to-square",
                            },
                            {
                                "title": "View my records of employment",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/roe/view.shtml",
                                "icon": "file-contract",
                            },
                            {
                                "title": "View my Employment Insurance documents",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/dus/view.shtml",
                                "icon": "folder-open",
                            },
                            {
                                "title": "View my Employment Insurance letters",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/dol/view.shtml",
                                "icon": "envelopes-bulk",
                            },
                            {
                                "title": "Submit documents for Employment Insurance",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/dus/instructions.shtml",
                                "icon": "file-import",
                            },
                            {
                                "title": "Submit eForms for Employment Insurance",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/eforms/landing.shtml",
                                "icon": "laptop-file",
                            },
                            {
                                "title": "Report a mistake",
                                "link": "https://www.canada.ca/en/services/benefits/ei/ei-regular-benefit/while-receiving.html#h2.08",
                                "icon": "file-exclamation",
                            },
                        ],
                    },
                    {
                        "title": "Personal information",
                        "tasks": [
                            {
                                "title": "Update my profile",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/contact-information/landing.shtml",
                                "icon": "circle-user",
                            },
                            {
                                "title": "Manage email notifications (Alert me)",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/alert-me/submit.shtml",
                                "icon": "bell",
                            },
                            {
                                "title": "Get my access code",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/access-code.shtml",
                                "icon": "key",
                            },
                            {
                                "title": "View my agreement status (self-employed) for Employment Insurance",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/self-employment/current-status.shtml",
                                "icon": "person-walking-luggage",
                            },
                        ],
                    },
                ],
            },
            {
                "id": "canada-pension-plan",
                "title": "Canada Pension Plan",
                "lists": [
                    {
                        "title": "Most requested",
                        "tasks": [
                            {
                                "title": "View my status updates for Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                "icon": "list-check",
                            },
                            {
                                "title": "View my Canada Pension Plan and Old Age Security payments ",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                "icon": "file-invoice-dollar",
                            },
                        ],
                    },
                    {
                        "title": "Applications",
                        "tasks": [
                            {
                                "title": "View my status updates for Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                "icon": "list-check",
                            },
                            {
                                "title": "Apply for Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/rtr-applicaton/step1-apply.shtml",
                                "icon": "stamp",
                            },
                            {
                                "title": "Apply for Canada Pension Plan Disability",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/ccpd-applicaton/application-in-progress.shtml",
                                "icon": "stamp",
                            },
                            {
                                "title": " Apply for Canada Pension Plan Death Benefits",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/cpp-death-benefits-general.shtml",
                                "icon": "stamp",
                            },
                            {
                                "title": "Apply for Canada Pension Plan Survivor's Pension and Children's Benefit",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/survivor-children-benefits/general-information.shtml",
                                "icon": "stamp",
                            },
                            {
                                "title": "Apply for Canada Pension Plan Survivor's Pension and Children's Benefit aged 18 to 25",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/child-benefits/general-information.shtml",
                                "icon": "stamp",
                            },
                        ],
                    },
                    {
                        "title": "Payments",
                        "tasks": [
                            {
                                "title": "View my Canada Pension Plan and Old Age Security payments ",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                "icon": "file-invoice-dollar",
                            },
                            {
                                "title": "View my Canada Pension Plan contributions",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/soc/earnings-contributions.shtml",
                                "icon": "hand-holding-dollar",
                            },
                            {
                                "title": "Estimate my retirement income for Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/soc/estimated-benefits.shtml",
                                "icon": "calculator",
                            },
                            {
                                "title": "Request a review of a decision for Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/request-reconsideration/step1-information-about-you.shtml",
                                "icon": "comments",
                            },
                        ],
                    },
                    {
                        "title": "Taxes",
                        "tasks": [
                            {
                                "title": "View my tax slips",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/tiso/view-tax-slips.shtml",
                                "icon": "receipt",
                            },
                            {
                                "title": "Change my tax deductions for the Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/fvtd/start.shtml",
                                "icon": "arrow-down-wide-short",
                            },
                            {
                                "title": "Change my tax slip delivery options",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/m sca/cpp-oas/tiso/delivery/change.shtml",
                                "icon": "envelope-open-text",
                            },
                        ],
                    },
                    {
                        "title": "Documents",
                        "tasks": [
                            {
                                "title": "Submit documents for Canada Pension Plan Disability",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/dus/step1-select-document.shtml",
                                "icon": "file-import",
                            },
                            {
                                "title": "Submit a declaration of attendance at school or university",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/declaration-attendance-school/step1-information-enrolment.shtml",
                                "icon": "school",
                            },
                        ],
                    },
                    {
                        "title": "Provisions",
                        "tasks": [
                            {
                                "title": "Request child-rearing provisions",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/crp/request-crp.shtml",
                                "icon": "baby-carriage",
                            },
                            {
                                "title": "View my child-rearing provision",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/crp/crp-information-with-children-option1.shtml",
                                "icon": "baby-carriage",
                            },
                            {
                                "title": "Apply for Canada Pension Plan credit split",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/cpp-credit-split/general-information.shtml",
                                "icon": "stamp",
                            },
                            {
                                "title": "Apply for Canada Pension Plan sharing ",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/cpp-pension-sharing/general-info.shtml",
                                "icon": "stamp",
                            },
                        ],
                    },
                    {
                        "title": "Personal information",
                        "tasks": [
                            {
                                "title": "Update my profile",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/contact-information/landing.shtml",
                                "icon": "circle-user",
                            },
                            {
                                "title": "Give consent to communicate on my behalf",
                                "link": "https://catalogue.servicecanada.gc.ca/content/EForms/en/Detail.html?Form=INS3280",
                                "icon": "user-check",
                            },
                        ],
                    },
                ],
            },
            {
                "id": "old-age-security",
                "title": "Old Age Security",
                "lists": [
                    {
                        "title": "Most requested",
                        "tasks": [
                            {
                                "title": "View my Old Age Security status updates ",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                "icon": "list-check",
                            },
                            {
                                "title": "View my Canada Pension Plan and Old Age Security payments ",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                "icon": "file-invoice-dollar",
                            },
                        ],
                    },
                    {
                        "title": "Applications",
                        "tasks": [
                            {
                                "title": "View my Old Age Security status updates ",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vmas/choose.shtml",
                                "icon": "list-check",
                            },
                            {
                                "title": "Apply for Old Age Security and Guaranteed Income Supplement",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/oas-gis-application/choose.shtml",
                                "icon": "stamp",
                            },
                            {
                                "title": "Apply for Guaranteed Income Supplement",
                                "link": "https://www.canada.ca/en/services/benefits/publicpensions/cpp/old-age-security/guaranteed-income-supplement/apply.html",
                                "icon": "stamp",
                            },
                            {
                                "title": "Apply for Allowance or Allowance for the Survivor",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/alw-alws/general-information.shtml",
                                "icon": "stamp",
                            },
                        ],
                    },
                    {
                        "title": "Payments",
                        "tasks": [
                            {
                                "title": "View my Canada Pension Plan and Old Age Security payments ",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/payment-information/details.shtml",
                                "icon": "file-invoice-dollar",
                            },
                            {
                                "title": "Delay receiving Old Age Security",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/vupi/delay-oas-gis/choose.shtml",
                                "icon": "clock-rotate-left",
                            },
                            {
                                "title": "Estimate my retirement income for Old Age Security",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/soc/estimated-benefits.shtml",
                                "icon": "calculator",
                            },
                            {
                                "title": "Request a review of a decision for Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/request-reconsideration/step1-information-about-you.shtml",
                                "icon": "comments",
                            },
                        ],
                    },
                    {
                        "title": "Taxes",
                        "tasks": [
                            {
                                "title": "View my tax slips",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/tiso/view-tax-slips.shtml",
                                "icon": "receipt",
                            },
                            {
                                "title": "Change my tax deductions for the Canada Pension Plan",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/cpp-oas/fvtd/start.shtml",
                                "icon": "arrow-down-wide-short",
                            },
                            {
                                "title": "Change my tax slip delivery options",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/m sca/cpp-oas/tiso/delivery/change.shtml",
                                "icon": "envelope-open-text",
                            },
                        ],
                    },
                    {
                        "title": "Personal information",
                        "tasks": [
                            {
                                "title": "Update my profile",
                                "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/ei/contact-information/landing.shtml",
                                "icon": "circle-user",
                            },
                            {
                                "title": "Give consent to communicate on my behalf",
                                "link": "https://catalogue.servicecanada.gc.ca/content/EForms/en/Detail.html?Form=INS3280",
                                "icon": "user-check",
                            },
                        ],
                    },
                ],
            },
        ],
        "exitBeta": {
            "title": "Exit Beta version",
            "link": "https://esdc.prv/en/service-canada/service-delivery/sda-assist/msca/view-change.shtml",
        },
    }
