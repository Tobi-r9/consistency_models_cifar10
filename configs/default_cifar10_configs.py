import ml_collections


def get_default_configs():
    config = ml_collections.ConfigDict()
    # training
    config.training = training = ml_collections.ConfigDict()
    training.batch_size = 128
    training.n_iters = 1300001
    training.snapshot_freq = 50000
    training.log_freq = 1000
    training.eval_freq = 1000
    ## store additional checkpoints for preemption in cloud computing environments
    training.snapshot_freq_for_preemption = 10000
    ## produce samples at each snapshot.
    training.snapshot_sampling = False
    training.likelihood_weighting = False
    training.n_jitted_steps = 5  # TODO: important flag!

    # sampling
    config.sampling = sampling = ml_collections.ConfigDict()
    sampling.n_steps_each = 1
    sampling.noise_removal = True
    sampling.probability_flow = False
    sampling.snr = 0.16

    # evaluation
    config.eval = evaluate = ml_collections.ConfigDict()
    evaluate.begin_ckpt = 9
    evaluate.end_ckpt = 26
    evaluate.batch_size = 512
    evaluate.enable_sampling = True
    evaluate.num_samples = 50000
    evaluate.enable_loss = True
    evaluate.enable_bpd = False
    evaluate.bpd_dataset = "test"

    # data
    config.data = data = ml_collections.ConfigDict()
    data.dataset = "CIFAR10"
    data.image_size = 32
    data.random_flip = True
    data.uniform_dequantization = False
    data.num_channels = 3

    # model
    config.model = model = ml_collections.ConfigDict()
    model.sigma_min = 0.02
    model.sigma_max = 100
    model.num_scales = 1000
    model.beta_min = 0.1
    model.beta_max = 20.0
    model.t_min = 0.002
    model.t_max = 80.0
    model.dropout = 0.1
    model.embedding_type = "fourier"
    model.double_heads = False

    # optimization
    config.optim = optim = ml_collections.ConfigDict()
    optim.weight_decay = 0.0
    optim.optimizer = "Adam"
    optim.lr = 2e-4
    optim.beta1 = 0.9
    optim.beta2 = 0.999
    optim.eps = 1e-8
    optim.warmup = 5000
    optim.grad_clip = 1.0
    optim.clip_sigmas = 5.0

    config.seed = 42

    return config
