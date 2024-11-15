# Ideas

Train from scratch on same ntt2

Larger / smaller SIR footprint (update loader to increase / decrease SIR mask)

More / fewer scenes (preproc from 2021 / filter with smaller delta T)

Higher resolution of SAR data (retrain c1, retrain some SIR models)

More AMSR2 bands on input (retrain c1, retrain some SIR models)

Process scenes and use derived SIR for training on other SAR images

Compute and plot conf. matrix

Plot SIR maps

Exclude some classes from training (update loader and config; or exclude extreme value and preproc dataset)

Merge some classes (update loader) or map classes to other SOD classes that were trained well

How much random rotation affects training.

Use MSE metrics and train on raw SIR, RFS

Use equal size clustering to normalize sampling


# Plan

1. Fix problem with model "m". Done!

2. Train from scratch two models, show that transfer learning is beneficial. If not, training with more input data or higher/lower SAR res can be done. Done.

3. Reduce number of scenes (filter by delta T) and train two models. Check effect of delta T. If strong, preproc of data from 2021 should be done. Done.

4. Increase and decrease SIR footprint (update loader) and train two models. If has effect, increase / decrease even more; train. Use the best footprint further.
Done. Unclear. Oversmapling of one class has higher effect.

5. Train _01d, _01e for checking effect of subsampling and more AMSR2 bands on SIC, SOD, FLOE.
Done. Unclear. Oversmapling of one class has higher effect.

6. Exclude some classes (update loader) and train two models. If helps, think how to limit data and preproc.

7. Switch off random rotation and train one model


# Status

models 02a - 02o are trained starting from 01c (SAR, AMSR, downsampling 2, SOD), each model for individual SIR##

models _02i and _02j have SIR09 and SIR08

model _02g failed to train. Probably bug in computing loss function when more classes (e.g. 127) are in the target.

model _02c1 is trained from scratch. Wandb project _02c is reused but workdirs _02c1 is created. Doesn't train as good as starting from _01c.

model _02c2 is trained from _01c with scenes with dT = 10 min. Score is a bit lower. Validation loss is MUCH larger.
Individual scores are about the same. Lower for class 0, higher for some other classes. No improvement.

models _02c3 and _02c4 are started from _01c with smaller and larger SIR footprint. Smaller footprint seemly gives better results.

models _01d and _01e are trained from scratch of SID,SOD,FLZ with downsample=1. _01d has same AMSR2 bands as _01c; _01e has all AMSR2 bands.
Scores are about the same in 1d/1e as in 1c. Strange that highest score is for class 0. Does it return just zeros everywhere?

models _04c1 and _04c2 are started from _01d and 01e with same params but for SIR02
Performance is similar to 02c. Again the highest score in Class 0.

models _04o1 and _04o2 are started from _01d and 01e with similar params but for SIR14

NB!
0th class is terribly oversmapled in ready_to_train (WATER) and in new_to_train (flat ice?)
So classification simply returns 0s everywhere in _1c- based models. That's how the score gets so high in 01c, and children.

Runs _01f and _01g EXCLUDE class 0. _01g does not randomly rotate.
Result - a bit better for class 10. Terrible for other classes.

Can we use transfer learning with bad model performance on ASIP data?!?!?!?!
