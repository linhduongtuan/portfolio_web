import reflex as rx
from ..components.styles import Size, Color, TextColor
from dataclasses import dataclass
from ..ui.base import base_page


@dataclass
class Publication:
    def __init__(
        self, title: str, authors: str, doi: str, year: int, abstract: str = ""
    ):
        self.title = title
        self.authors = authors
        self.doi = doi
        self.year = year
        self.abstract = abstract


def publication_item(pub: Publication) -> rx.Component:
    """Create a publication item component."""
    return rx.vstack(
        rx.hstack(
            rx.text("•", color=TextColor.PRIMARY.value),
            rx.vstack(
                rx.text(
                    f"{pub.authors},",
                    color=TextColor.PRIMARY.value,
                    font_weight="medium",
                ),
                rx.text(
                    f'"{pub.title}"',
                    font_style="italic",
                    color=TextColor.PRIMARY.value,
                ),
                rx.hstack(
                    rx.text(
                        "DOI:",
                        color=TextColor.PRIMARY.value,
                        font_weight="medium",
                    ),
                    rx.link(
                        pub.doi,
                        href=pub.doi,
                        is_external=True,
                        text_decoration="underline",
                        color=TextColor.PRIMARY.value,
                        _hover={
                            "color": Color.PRIMARY.value,
                            "text_decoration": "none",
                        },
                    ),
                ),
                align_items="start",
                width="100%",
            ),
            width="100%",
        ),
        rx.accordion.root(
            rx.accordion.item(
                header="Show Abstract",
                content=rx.text(
                    pub.abstract,
                    color=TextColor.PRIMARY.value,
                    font_size=Size.DEFAULT.value,
                    font_style="italic",
                ),
                bg=Color.SECONDARY.value,
                padding="1em",
                border_radius="0.5em",
                width="100%",
                # Optional: add hover effect
                _hover={
                    "bg": "rgba(0,0,0,0.8)",  # slightly transparent black
                },
                # Optional: add transition
                transition="all 0.2s ease-in-out",
            ),
            collapsible=True,
            width="1000px",
            type="multiple",
        ),
        align_items="start",
        width="100%",
        spacing="3",
    )


def year_section(year: int, pubs: list[Publication]) -> rx.Component:
    year_pubs = [p for p in pubs if p.year == year]
    if not year_pubs:
        return rx.box()

    return rx.box(
        rx.heading(
            str(year),
            size=Size.GARGANTUAL.value,  # type: ignore
            margin_y="1em",
            color=TextColor.PRIMARY.value,
        ),
        rx.vstack(
            *[publication_item(pub) for pub in year_pubs],
            align_items="start",
            spacing="2",
            padding_left="1em",
        ),
        margin_bottom="2em",
    )


@rx.page(route="/publications")
def publications_view() -> rx.Component:
    years = range(2024, 2015, -1)

    my_child = rx.box(
        rx.vstack(
            rx.heading(
                "PUBLICATIONS",
                size=Size.BIG.value,  # type: ignore
                color=TextColor.PRIMARY.value,
                margin_bottom="0.5em",  # Space below the heading
                font_size="3em",  # Or use direct size
                font_weight="bold",  # Optional: make it bolder
                align_self="center",  # Center it horizontally
                # Or align_self="flex-start" for left alignment
                # Or align_self="flex-end" for right alignment
                padding_top="1em",  # Space above the heading
            ),
            *[year_section(year, PUBLICATIONS) for year in years],
            align_items="start",
            spacing="4",
            width="100%",
            max_width="1200px",
            margin="0 auto",
            padding="2em",
            color=TextColor.PRIMARY.value,
            size=Size.HUGE.value,
            id="my-child",
        ),
    )
    return base_page(my_child)


PUBLICATIONS = [
    Publication(
        title="Automated fruit recognition using EfficientNet and MixNet",
        authors="Linh T Duong, Phuong T Nguyen, Claudio Di Sipio, Davide Di Ruscio",
        doi="https://doi.org/10.1016/j.compag.2020.105326",
        year=2020,
        abstract="The classification of fruits offers many useful applications in daily life, such as automated harvesting or building up stocks for supermarkets. Studies have been proposed to classify fruits from input images, exploiting image processing and machine learning techniques. Though a lot of improvements have been achieved in recent years, many approaches still suffer prolonged training/testing time, or a considerably high number of false positives. For several applications, it is crucial to provide users with not only precise but also real-time recommendations. In this paper, we propose a practical solution to fruit recognition by exploiting two recently-developed classifiers that have demonstrated themselves to be both effective and efficient. We adopted EfficientNet and MixNet, two families of deep neural networks to build an expert system being able to accurately and swiftly identify fruits. Such a system can be deployed onto devices with limited computational resources to prompt exact and timely recommendations. The approach’s performance has been validated on a real dataset consisting of 48,905 images for training and 16,421 images for testing. The experimental results showed that the application of EfficientNet and MixNet on the considered dataset substantially improves the overall prediction accuracy in comparison to a well-established baseline.",
    ),
    Publication(
        title="Detection of tuberculosis from chest X-ray images: Boosting the performance with vision transformer and transfer learning",
        authors="Linh T. Duong, Nhi H. Le, Toan B. Tran, Vuong M. Ngo, Phuong T. Nguyen",
        doi="https://doi.org/10.1016/j.eswa.2021.115519",
        year=2021,
        abstract="Tuberculosis (TB) caused by Mycobacterium tuberculosis is a contagious disease which is among the top deadly diseases in the world. Research in Medical Imaging has been done to provide doctors with techniques and tools to early detect, monitor and diagnose the disease using Artificial Intelligence. Recently, many attempts have been made to automatically recognize TB from chest X-ray (CXR) images. Still, while the obtained performance is encouraging, according to our investigation, many of the existing approaches have been evaluated on small and undiverse datasets. We suppose that such a good performance might not hold for heterogeneous data sources, which originate from real world scenarios. Our present work aims to fill the gap and improve the prediction performance on larger datasets. In particular, we present a practical solution for the detection of tuberculosis from CXR images, making use of cutting-edge Machine Learning and Computer Vision algorithms. We conceptualize a framework by adopting three recent deep neural networks as the main classification engines, namely modified EfficientNet, modified original Vision Transformer, and modified Hybrid EfficientNet with Vision Transformer. Moreover, we also empower the learning process with various augmentation techniques. We evaluated the proposed approach using a large dataset which has been curated by merging various public datasets. The resulting dataset has been split into training, validation, and testing sets which account for 80%, 10%, and 10% of the original dataset, respectively. To further study our proposed approach, we compared it with two state-of-the-art systems. The obtained results are encouraging: the maximum accuracy of 97.72% with AUC of 100% is achieved with ViT_Base_EfficientNet_B1_224. The experimental results demonstrate that our conceived tool outperforms the considered baselines with respect to different quality metrics.",
    ),
    Publication(
        title="Automatic detection of Covid-19 from chest X-ray and lung computed tomography images using deep neural networks and transfer learning",
        authors="Linh T. Duong, Phuong T. Nguyen, Ludovico Iovino, Michele Flammini",
        doi="https://doi.org/10.1016/j.asoc.2022.109851",
        year=2023,
        abstract="The world has been undergoing the most ever unprecedented circumstances caused by the coronavirus pandemic, which is having a devastating global effect in different aspects of life. Since there are not effective antiviral treatments for Covid-19 yet, it is crucial to early detect and monitor the progression of the disease, thereby helping to reduce mortality. While different measures are being used to combat the virus, medical imaging techniques have been examined to support doctors in diagnosing the disease. In this paper, we present a practical solution for the detection of Covid-19 from chest X-ray (CXR) and lung computed tomography (LCT) images, exploiting cutting-edge Machine Learning techniques. As the main classification engine, we make use of EfficientNet and MixNet, two recently developed families of deep neural networks. Furthermore, to make the training more effective and efficient, we apply three transfer learning algorithms. The ultimate aim is to build a reliable expert system to detect Covid-19 from different sources of images, making it be a multi-purpose AI diagnosing system. We validated our proposed approach using four real-world datasets. The first two are CXR datasets consist of 15,000 and 17,905 images, respectively. The other two are LCT datasets with 2,482 and 411,528 images, respectively. The five-fold cross-validation methodology was used to evaluate the approach, where the dataset is split into five parts, and accordingly the evaluation is conducted in five rounds. By each evaluation, four parts are combined to form the training data, and the remaining one is used for testing. We obtained an encouraging prediction performance for all the considered datasets. In all the configurations, the obtained accuracy is always larger than 95.0%. Compared to various existing studies, our approach yields a substantial performance gain. Moreover, such an improvement is statistically significant.",
    ),
    Publication(
        title="GvmR – A Novel LysR-Type Transcriptional Regulator Involved in Virulence and Primary and Secondary Metabolism of Burkholderia pseudomallei",
        authors="Linh Tuan Duong, Sandra Schwarz, Harald Gross, Katrin Breitbach, Falko Hochgräfe, Jörg Mostertz, Kristin Eske-Pogodda, Gabriel E Wagner, Ivo Steinmetz, Christian Kohler",
        doi=" https://doi.org/10.3389/fmicb.2018.00935",
        year=2018,
        abstract="Burkholderia pseudomallei is a soil-dwelling bacterium able to survive not only under adverse environmental conditions, but also within various hosts which can lead to the disease melioidosis. The capability of B. pseudomallei to adapt to environmental changes is facilitated by the large number of regulatory proteins encoded by its genome. Among them are more than 60 uncharacterized LysR-type transcriptional regulators (LTTRs). Here we analyzed a B. pseudomallei mutant harboring a transposon in the gene BPSL0117 annotated as a LTTR, which we named gvmR (globally acting virulence and metabolism regulator). The gvmR mutant displayed a growth defect in minimal medium and macrophages in comparison with the wild type. Moreover, disruption of gvmR rendered B. pseudomallei avirulent in mice indicating a critical role of GvmR in infection. These defects of the mutant were rescued by ectopic expression of gvmR. To identify genes whose expression is modulated by GvmR, global transcriptome analysis of the B. pseudomallei wild type and gvmR mutant was performed using whole genome tiling microarrays. Transcript levels of 190 genes were upregulated and 141 genes were downregulated in the gvmR mutant relative to the wild type. Among the most downregulated genes in the gvmR mutant were important virulence factor genes (T3SS3, T6SS1, and T6SS2), which could explain the virulence defect of the gvmR mutant. In addition, expression of genes related to amino acid synthesis, glyoxylate shunt, iron-sulfur cluster assembly, and syrbactin metabolism (secondary metabolite) was decreased in the mutant. On the other hand, inactivation of GvmR increased expression of genes involved in pyruvate metabolism, ATP synthesis, malleobactin, and porin genes. Quantitative real-time PCR verified the differential expression of 27 selected genes. In summary, our data show that GvmR acts as an activating and repressing global regulator that is required to coordinate expression of a diverse set of metabolic and virulence genes essential for the survival in the animal host and under nutrient limitation.",
    ),
    Publication(
        title="Fusion of edge detection and graph neural networks to classifying electrocardiogram signals",
        authors="Linh T. Duong, Thu T.H. Doan, Cong Q. Chu, Phuong T. Nguyen",
        doi="https://doi.org/10.1016/j.eswa.2023.120107",
        year=2023,
        abstract="The analysis of electrocardiogram (ECG) signals are among the key factors in the diagnosis of cardiovascular diseases (CVDs). However, automatic processing of ECG in clinical practice is still restrained by the accuracy of existing algorithms. Deep learning methods have recently achieved striking success in a variety of task including predictive healthcare. Graph neural networks are a class of machine learning algorithms which can learn by directly extracting important information from graph-structured data, and perform prediction on unknown data. Such algorithms are suitable for mining complex graph data, deducing useful predictions. In this work, we present a Graph Neural Network (GNN) model trained in two datasets with more than 107,000 single-lead signal images extracted from laboratories of Boston’s Beth Israel Hospital and of the Massachusetts Institute of Technology (MITBIH), and 1.5 million labeled exams analyzed by the Physikalisch-Technische Bundesanstalt (PTB). Our proposed GNN achieves promising performance, i.e., the results show that ECG classification based on GNNs using either single-lead or 12-lead setup is closer to the human-level in standard clinical practice. By several testing instances, the proposed approach obtains an accuracy of 1.0, thereby outperforming various state-of-the-art baselines by both databases with respect to effectiveness and timing efficiency. We anticipate that the approach can be deployed as a non-invasive pre-screening tool to assist doctors in real-time monitoring and performing their diagnosis activities.",
    ),
    Publication(
        title="First report on association of hyperuricemia with type 2 diabetes in a vietnamese population",
        authors="Tran Quang Binh, Pham Tran Phuong, Nguyen Thanh Chung, Bui Thi Nhung, Do Dinh Tung, Tran Quang Thuyen, Tuan Linh Duong, Thuy Nga, Bui Thi, Nguyen Anh Ngoc, Danh Le Tuyen",
        doi=" https://doi.org/10.1155/2019/5275071",
        year=2019,
        abstract="Background. Uric acid is a powerful free-radical scavenger in humans, but hyperuricemia may induce insulin resistance and beta-cell dysfunction. The study aimed to evaluate the association between hyperuricemia and hyperglycemia, considering the confounding factors in a Vietnamese population. Methods. A population-based cross-sectional study recruited 1542 adults aged 50 to 70 years to collect data on socioeconomic status, lifestyle factors, and clinical patterns. Associations between hyperuricemia and hyperglycemia (isolated impaired fasting glucose (IFG), isolated impaired glucose tolerance (IGT), combined IFG-IGT, and type 2 diabetes (T2D)) were evaluated by multinomial logistic regression analysis in several models, adjusting for the confounding factors including socioeconomic status, lifestyle factors, and clinical measures. Results. Uric acid values were much higher in IFG, IFG-IGT, and T2D groups compared to those in the normal glucose tolerance (NGT) group. The significant association of hyperuricemia with IFG, IFG-IGT, and T2D was found in the model unadjusted and remained consistently in several models adjusted for socioeconomic status, lifestyle factors, and clinical patterns. In the final model, the consistent hyperglycemia risk was found in total sample (OR = 2.23 for IFG, OR = 2.29 for IFG-IGT, and 1.75 for T2D, P ≤ 0.006) and in women (OR = 2.90 for IFG, OR = 3.96 for IFG-IGT, and OR = 2.49 for T2D, P < 0.001) but not in men. Conclusions. It is the first report in Vietnamese population suggesting the significant association of hyperuricemia with IFG, IFG-IGT, and T2D; and the predominant association was found in women than in men, taken into account the confounding factors.",
    ),
    Publication(
        authors="Bui Thi Binh, Tran Quang and Duong, Tuan Linh and Chung, Le Thi Kim and Phuong, Pham Tran and Nga, Bui Thi Thuy and Ngoc, Nguyen Anh and Thuyen, Tran Quang and Tung, Do Dinh and Nhung",
        title="FTO-rs9939609 Polymorphism is a Predictor of Future Type 2 Diabetes: A Population-Based Prospective Study",
        doi="https://doi.org/10.1007/s10528-021-10124-0",
        year=2022,
        abstract="The study aimed to evaluate the contribution of the FTO A/T polymorphism (rs9939609) to the prediction of the future type 2 diabetes (T2D). A population-based prospective study included 1443 nondiabetic subjects at baseline, and they were examined for developing T2D after 5-year follow-up. Cox proportional hazards model was used to evaluate the hazard ratio (HR) of rs9939609 to the future T2D in the models adjusted for the confounding factors including socio-economic status, lifestyle factors (smoking and drinking history, sporting habits, and leisure time), and clinical patterns (obese status, blood pressures, and dyslipidemia) at baseline. The area under receiver operating characteristic curve (AUC) was used to measure the power to predict individuals with T2D. The FTO-rs9939609 polymorphism was a significant predictor of future T2D in the model unadjusted, and it remained significant in the final model after adjustment for the confounding factors, showing an additive effect of the A-allele (HR = 1.35, 95% CI = 1.02–1.78, P = 0.036, AUC = 0.676). For normoglycemic subjects at baseline, the similar final adjusted model reported the increased HR per A-allele (HR = 1.50, 95% CI = 1.09–2.07, P = 0.012, AUC = 0.697). Five-year changes in BMI, waist circumference, and systolic blood pressure did not remove the contribution of rs9939609 to increased HR of T2D. The population attributable risk for risk genotype was 13.6%. In conclusion, the study indicates that the FTO-rs9939609 polymorphism is an important genetic predictor for future T2D in Vietnamese population.",
    ),
    Publication(
        title="Deep Learning for Automated Recognition of Covid-19 from Chest X-ray Images",
        authors="Tuan Linh Duong, Ludovico Iovino, Michele Flammini, Thanh Phuong Nguyen",
        doi="https://doi.org/10.1101/2020.08.13.20173997",
        year=2020,
        abstract="The pandemic caused by coronavirus in recent months is having a devastating global effect, which puts the world under the most ever unprecedented emergency. Currently, since there are not effective antiviral treatments for Covid-19 yet, it is crucial to early detect and monitor the progression of the disease, thus helping to reduce mortality. While a corresponding vaccine is being developed, and different measures are being used to combat the virus, medical imaging techniques have also been investigated to assist doctors in diagnosing this disease. Objective: This paper presents a practical solution for the detection of Covid-19 from chest X-ray (CXR) images, exploiting cutting-edge Machine Learning techniques. Methods: We employ EfficientNet and MixNet, two recently developed families of deep neural networks, as the main classification engine. Furthermore, we also apply different transfer learning strategies, aiming at making the training process more accurate and efficient. The proposed approach has been validated by means of two real datasets, the former consists of 13,511 training images and 1,489 testing images, the latter has 14,324 and 3,581 images for training and testing, respectively. Results: The results are promising: by all the experimental configurations considered in the evaluation, our approach always yields an accuracy larger than 95.0%, with the maximum accuracy obtained being 96.64%. Conclusions: As a comparison with various existing studies, we can thus conclude that our performance improvement is significant.",
    ),
    Publication(
        title="High incidence of type 2 diabetes in a population with normal range body mass index and individual prediction nomogram in Vietnam",
        authors="Binh Tran Quang, Phuong Pham Tran, Chung Nguyen Thanh, Nhung Bui Thi, Tung Do Dinh, Thuyen Tran Quang, Tuan Linh Duong, Nga Bui Thi Thuy, Ngoc Nguyen Anh",
        doi="https://doi.org/10.1111/dme.14680",
        year=2022,
        abstract="The study aimed at determining 5-year incidence and prediction nomogram for new-onset type 2 diabetes (T2D) in a middle-aged population in Vietnam. A population-based prospective study was designed to collect socio-economic, anthropometric, lifestyle and clinical data. Five-year T2D incidence was estimated and adjusted for age and sex. Hazard ratio (HR) for T2D was investigated using discrete-time proportional hazards model. T2D prediction model entering the most significant risk factors was developed using the multivariable logistic-regression algorithm. The corresponding prediction nomogram was constructed and checked for discrimination, calibration and clinical usefulness. The age- and sex-adjusted incidence was 21.0 cases (95% CI: 12.2−40.0) per 1000 person-years in people with mean BMI of 22.2 (95% CI: 21.9−22.7 kg/m2). The HRs (95% CI) for T2D were 1.14 (1.05−1.23) per 10 mmHg systolic blood pressure, 1.05 (1.03−1.08) per 1 cm waist circumference, 1.40 (1.13−1.73) per 1 mmol/L fasting blood glucose, 1.77 (1.15−2.71) per sleeping time (<6 h/day vs 6–7 h/day) and 2.12 (1.25−3.61) per residence (urban vs rural). The prediction nomogram for new-onset T2D had a good discrimination (area under curve: 0.711, 95% CI: 0.666−0.755) and fit calibration (mean absolute error: 0.009). For the predicted probability thresholds between 0.03 and 0.36, the nomogram showed a positive net benefit, without increasing the number of false positives. This study highlighted an alarmingly high incidence of T2D in a middle-aged population with a normal range BMI in Vietnam. The individual prediction nomogram with decision curve analysis for new-onset T2D would be valuable for early detection, intervention and treatment of the condition.",
    ),
    Publication(
        title="Incidence and prediction nomogram for metabolic syndrome in a middle-aged Vietnamese population: a 5-year follow-up study",
        authors="Tran Quang Thuyen, Dinh Hong Duong, Bui Thi Thuy Nga, Nguyen Anh Ngoc, Tuan Linh Duong, Pham Tran Phuong, Bui Thi Nhung, Tran Quang Binh",
        doi="https://doi.org/10.1007/s12020-021-02836-5",
        year=2022,
        abstract="We aimed to determine the incidence and prediction nomogram for new-onset metabolic syndrome (MetS) in a middle-aged Vietnamese population. A population-based prospective study was conducted in 1150 participants aged 40–64 years without MetS at baseline and followed-up for 5 years. Data on lifestyle factors, socioeconomic status, family diabetes history, and anthropometric measures were collected. MetS incidence was estimated in general population and subgroup of age, gender, and MetS components. A Cox proportional hazards regression was used to estimate hazard ratios (HRs) with 95% confidence intervals (CI) for MetS. A prediction nomogram was developed and checked for discrimination and calibration. During median follow-up of 5.14 years, the accumulate MetS incidence rate was 23.4% (95% CI: 22.2–24.7). The annual incidence rate (95% CI) was 52.9 (46.7–60.1) per 1000 person-years in general population and higher in women [56.6 (48.7–65.9)] than men [46.5 (36.9–59.3)]. The HRs (95% CI) for developing MetS were gender [females vs males: 2.04 (1.26–3.29)], advanced age [1.02 (1.01–1.04) per one year], waist circumference [1.08 (1.06–1.10) per one cm] and other obesity-related traits, and systolic blood pressure [1.02 (1.01–1.03) per one mmHg]. The prediction nomogram for MetS had a good discrimination (C-statistics = 0.742) and fit calibration (mean absolute error = 0.009) with a positive net benefit in the predicted probability thresholds between 0.13 and 0.70. The study is the first to indicate an alarmingly high incidence of MetS in a middle-aged population in Vietnam. The nomogram with simply applicable variables would be useful to qualify individual risk of developing MetS.",
    ),
    Publication(
        title="Automatic detection of weeds: synergy between EfficientNet and transfer learning to enhance the prediction accuracy",
        authors="Linh T Duong, Toan B Tran, Nhi H Le, Vuong M Ngo, Phuong T Nguyen",
        doi="https://doi.org/10.1007/s00500-023-09212-7",
        year=2023,
        abstract="The application of digital technologies to facilitate farming activities has been on the rise in recent years. Among different tasks, the classification of weeds is a prerequisite for smart farming, and various techniques have been proposed to automatically detect weeds from images. However, many studies deal with weed images collected in the laboratory settings, and this might not be applicable to real-world scenarios. In this sense, there is still the need for robust classification systems that can be deployed in the field. In this work, we propose a practical solution to recognition of weeds exploiting two versions of EfficientNet as the recommendation engine. More importantly, to make the learning more effective, we also utilize different transfer learning strategies. The final aim is to build an expert system capable of accurately detecting weeds from lively captured images. We evaluate the approach’s performance using DeepWeeds, a real-world dataset with 17,509 images. The experimental results show that the application of EfficientNet and transfer learning on the considered dataset substantially improves the overall prediction accuracy in various settings. Through the evaluation, we also demonstrate that the conceived tool outperforms various state-of-the-art baselines. We expect that the proposed framework can be installed in robots to work on rice fields in Vietnam, allowing farmers to find and eliminate weeds in an automatic manner.",
    ),
    Publication(
        title="Edge detection and graph neural networks to classify mammograms: A case study with a dataset from Vietnamese patients",
        authors="Linh T. Duong, Cong Q. Chu, Phuong T. Nguyen, Son T. Nguyen, Binh Q. Tran",
        doi="https://doi.org/10.1016/j.asoc.2022.109974",
        year=2022,
        abstract="Mammograms are breast X-ray images and they are used by doctors, among other purposes, as an effective means of detecting breast cancer. Screening mammography is crucial since it allows doctors to understand better the situation and have suitable intervention. The classification of medical modalities is a prerequisite for development of computer-aided diagnosis tools in healthcare, and various techniques have been proposed to automatically classify from mammography images. Though there have been several tools developed, they have been mostly validated with data collected from Western women. Based on our initial investigations, breast anatomy in Vietnamese women differs from that of Western women, due to denser breast tissue. In this paper, we propose MammoGNN – a practical solution to the classification of mammograms using the synergy between image processing techniques and graph neural networks. First, a well-founded edge detection algorithm was applied to provide input for the recommendation engine. Afterward, we empirically experimented to select suitable graph neural networks to manage the training and prediction. A mammogram dataset was curated from 2,351 Vietnamese women to validate the conceived tool. By several testing instances, MammoGNN obtains a maximum accuracy of 100%, precision and recall of 1.0 on independent and shuffle test sets for both classification of BI-RADS scores and breast density types. The experimental results also demonstrate that our proposed approach obtains an optimal prediction performance on the considered datasets, outperforming different baselines. We anticipate that the proposed approach can be deployed as a non-invasive pre-screening tool to assist doctors in performing their diagnosis activities.",
    ),
    Publication(
        title="A simple nomogram for identifying individuals at high risk of undiagnosed diabetes in rural population",
        authors="Tran Quang Binh, Pham Tran Phuong, Nguyen Thanh Chung, Bui Thi Nhung, Do Dinh Tung, Tuan Linh Duong, Tran Ngoc Luong, Le Danh Tuyen",
        doi="https://doi.org/10.1016/j.diabres.2021.109061",
        year=2021,
        abstract="To sought for an easily applicable nomogram for detecting individuals at high risk of undiagnosed type 2 diabetes.The development cohort included 2542 participants recruited randomly from a rural population in 2011. The glycemic status of subjects was determined using the fasting plasma glucose test and the oral glucose tolerance test. The Bayesian Model Average approach was used to search for a parsimonious model with minimum number of predictor and maximum discriminatory power. The corresponding prediction nomograms were constructed and checked for discrimination, calibration, clinical usefulness, and generalizability in nationwide population in 2012. The non-lab nomogram including waist circumference and systolic blood pressure was the most parsimonious with the area under receiver operating characteristic curve (AUC) of 0.71 (95 %CI = 0.64–0.76). Adding low-density lipoprotein cholesterol in the non-lab nomogram generated the lab-based nomogram with significantly improved AUC of 0.83 (0.78–0.87, P < 0.001). The nomograms had a positive net benefit at threshold probability between 0.01 and 0.15. Applying the non-lab nomogram to the national population yielded the AUC of 0.66 (0.63–0.70) and 0.68 (0.65–0.71) in the cohorts aged 40–64 and 30–69 years, respectively. The novel nomograms could help promote the early detection of undiagnosed diabetes in rural Vietnamese population.",
    ),
    Publication(title="", authors="", doi="", year=202, abstract=""),
    Publication(title="", authors="", doi="", year=202, abstract=""),
]
