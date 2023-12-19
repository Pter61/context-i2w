<div align="center">
	
# Context-I2W: Mapping Images to Context-dependent words for Accurate Zero-Shot Composed Image Retrieval (AAAI 2024)
[![arXiv](https://img.shields.io/badge/arXiv-Context-I2W.svg?logo=arXiv)](https://arxiv.org/abs/2309.16137)
[![License](https://img.shields.io/badge/License-MIT-green.svg)]()
[![GitHub Stars](https://img.shields.io/github/stars/Pter61/context-i2w?style=social)](https://github.com/Pter61/context-i2w)

	
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/context-i2w-mapping-images-to-context/zero-shot-composed-image-retrieval-zs-cir-on-4)](https://paperswithcode.com/sota/zero-shot-composed-image-retrieval-zs-cir-on-4?p=context-i2w-mapping-images-to-context) <br/>
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/context-i2w-mapping-images-to-context/zero-shot-composed-image-retrieval-zs-cir-on-6)](https://paperswithcode.com/sota/zero-shot-composed-image-retrieval-zs-cir-on-6?p=context-i2w-mapping-images-to-context) <br/>
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/context-i2w-mapping-images-to-context/zero-shot-composed-image-retrieval-zs-cir-on-2)](https://paperswithcode.com/sota/zero-shot-composed-image-retrieval-zs-cir-on-2?p=context-i2w-mapping-images-to-context) <br/>
[![PWC](https://img.shields.io/endpoint.svg?url=https://paperswithcode.com/badge/context-i2w-mapping-images-to-context/zero-shot-composed-image-retrieval-zs-cir-on-1)](https://paperswithcode.com/sota/zero-shot-composed-image-retrieval-zs-cir-on-1?p=context-i2w-mapping-images-to-context)
</div>

![Context-I2W](context-i2w.jpg)

<div align="justify">

> Different from Composed Image Retrieval task that requires expensive labels for training task-specific models, Zero-Shot Composed Image Retrieval (ZS-CIR) involves diverse tasks with a broad range of visual content manipulation intent that could be related to domain, scene, object, and attribute. The key challenge for ZS-CIR tasks is to learn a more accurate image representation that has adaptive attention to the reference image for various manipulation descriptions. In this paper, we propose a novel context-dependent mapping network, named Context-I2W,  for adaptively converting description-relevant Image information into a pseudo-word token composed of the description for accurate ZS-CIR. Specifically, an Intent View Selector first dynamically learns a rotation rule to map the identical image to a task-specific manipulation view. Then a Visual Target Extractor further captures local information covering the main targets in ZS-CIR tasks under the guidance of multiple learnable queries. The two complementary modules work together to map an image to a context-dependent pseudo-word token without extra supervision. Our model shows strong generalization ability on four ZS-CIR tasks, including domain conversion, object composition, object manipulation, and attribute manipulation. It obtains consistent and significant performance boosts ranging from 1.88% to 3.60% over the best methods and achieves new state-of-the-art results on ZS-CIR.

</div>

## Description
This repository contains the code for the paper ["Context-I2W: Mapping Images to Context-dependent words for Accurate Zero-Shot Composed Image Retrieval"](https://arxiv.org/abs/2309.16137).

### Contribution
1. We **consider manipulation descriptions and learnable queries multi-level constraints for visual information filtering**, which sheds new light on the vision-to-language alignment mechanism.
2.  Our Intent View Selector and Visual Target Extractor selectively **map images dependent on the context of manipulation descriptions**, enhancing the ability of the CLIP Language Encoder to generalize images to complex manipulation descriptions effectively.
3.  Our Context-I2W is **the first to mask the object name while retaining the original caption in CIR tasks**. It builds on the insight that context clues should be paid more attention to in the objective, which is an interesting insight that will motivate future works.
   
## TODO 
1. Inference code and checkpoints
2. Training code
